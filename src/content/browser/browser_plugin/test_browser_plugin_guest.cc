// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "content/browser/browser_plugin/test_browser_plugin_guest.h"

#include "base/test/test_timeouts.h"
#include "content/browser/renderer_host/render_view_host_impl.h"
#include "content/browser/web_contents/web_contents_impl.h"
#include "content/common/browser_plugin/browser_plugin_messages.h"

namespace content {

class BrowserPluginGuest;

TestBrowserPluginGuest::TestBrowserPluginGuest(
    int instance_id,
    WebContentsImpl* web_contents)
    : BrowserPluginGuest(instance_id, false, web_contents),
      update_rect_count_(0),
      exit_observed_(false),
      focus_observed_(false),
      blur_observed_(false),
      advance_focus_observed_(false),
      input_observed_(false),
      load_stop_observed_(false),
      ime_cancel_observed_(false) {
}

TestBrowserPluginGuest::~TestBrowserPluginGuest() {
}

WebContentsImpl* TestBrowserPluginGuest::web_contents() const {
  return static_cast<WebContentsImpl*>(BrowserPluginGuest::web_contents());
}

void TestBrowserPluginGuest::SendMessageToEmbedder(IPC::Message* msg) {
  if (msg->type() == BrowserPluginMsg_UpdateRect::ID) {
    update_rect_count_++;
    int instance_id = 0;
    BrowserPluginMsg_UpdateRect_Params params;
    BrowserPluginMsg_UpdateRect::Read(msg, &instance_id, &params);
    last_view_size_observed_ = params.view_size;
    if (!expected_auto_view_size_.IsEmpty() &&
        expected_auto_view_size_ == params.view_size) {
      if (auto_view_size_message_loop_runner_)
        auto_view_size_message_loop_runner_->Quit();
    }
    if (send_message_loop_runner_)
      send_message_loop_runner_->Quit();
  }
  BrowserPluginGuest::SendMessageToEmbedder(msg);
}

void TestBrowserPluginGuest::WaitForUpdateRectMsg() {
  // Check if we already got any UpdateRect message.
  if (update_rect_count_ > 0)
    return;
  send_message_loop_runner_ = new MessageLoopRunner();
  send_message_loop_runner_->Run();
}

void TestBrowserPluginGuest::ResetUpdateRectCount() {
  update_rect_count_ = 0;
}

void TestBrowserPluginGuest::RenderProcessGone(base::TerminationStatus status) {
  exit_observed_ = true;
  if (status != base::TERMINATION_STATUS_NORMAL_TERMINATION &&
      status != base::TERMINATION_STATUS_STILL_RUNNING)
    VLOG(0) << "Guest crashed status: " << status;
  if (crash_message_loop_runner_)
    crash_message_loop_runner_->Quit();
  BrowserPluginGuest::RenderProcessGone(status);
}

void TestBrowserPluginGuest::OnHandleInputEvent(
    int instance_id,
    const gfx::Rect& guest_window_rect,
    const blink::WebInputEvent* event) {
  BrowserPluginGuest::OnHandleInputEvent(instance_id,
                                         guest_window_rect,
                                         event);
  input_observed_ = true;
  if (input_message_loop_runner_)
    input_message_loop_runner_->Quit();
}

void TestBrowserPluginGuest::WaitForExit() {
  // Check if we already observed a guest crash, return immediately if so.
  if (exit_observed_)
    return;

  crash_message_loop_runner_ = new MessageLoopRunner();
  crash_message_loop_runner_->Run();
}

void TestBrowserPluginGuest::WaitForFocus() {
  if (focus_observed_) {
    focus_observed_ = false;
    return;
  }
  focus_message_loop_runner_ = new MessageLoopRunner();
  focus_message_loop_runner_->Run();
  focus_observed_ = false;
}

void TestBrowserPluginGuest::WaitForBlur() {
  if (blur_observed_) {
    blur_observed_ = false;
    return;
  }
  blur_message_loop_runner_ = new MessageLoopRunner();
  blur_message_loop_runner_->Run();
  blur_observed_ = false;
}

void TestBrowserPluginGuest::WaitForAdvanceFocus() {
  if (advance_focus_observed_)
    return;
  advance_focus_message_loop_runner_ = new MessageLoopRunner();
  advance_focus_message_loop_runner_->Run();
}

void TestBrowserPluginGuest::WaitForInput() {
  if (input_observed_) {
    input_observed_ = false;
    return;
  }

  input_message_loop_runner_ = new MessageLoopRunner();
  input_message_loop_runner_->Run();
  input_observed_ = false;
}

void TestBrowserPluginGuest::WaitForLoadStop() {
  if (load_stop_observed_) {
    load_stop_observed_ = false;
    return;
  }

  load_stop_message_loop_runner_ = new MessageLoopRunner();
  load_stop_message_loop_runner_->Run();
  load_stop_observed_ = false;
}

void TestBrowserPluginGuest::WaitForViewSize(const gfx::Size& view_size) {
  if (last_view_size_observed_ == view_size) {
    last_view_size_observed_ = gfx::Size();
    return;
  }

  expected_auto_view_size_ = view_size;
  auto_view_size_message_loop_runner_ = new MessageLoopRunner();
  auto_view_size_message_loop_runner_->Run();
  last_view_size_observed_ = gfx::Size();
}

void TestBrowserPluginGuest::WaitForImeCancel() {
  if (ime_cancel_observed_) {
    ime_cancel_observed_ = false;
    return;
  }

  ime_cancel_message_loop_runner_ = new MessageLoopRunner();
  ime_cancel_message_loop_runner_->Run();
  ime_cancel_observed_ = false;
}

void TestBrowserPluginGuest::WaitForResizeGuest(const gfx::Size& view_size) {
  if (last_size_observed_in_resize_ == view_size) {
    last_size_observed_in_resize_ = gfx::Size();
    return;
  }

  expected_view_size_in_resize_ = view_size;
  resize_guest_message_loop_runner_ = new MessageLoopRunner();
  resize_guest_message_loop_runner_->Run();
  last_size_observed_in_resize_ = gfx::Size();
}

void TestBrowserPluginGuest::OnSetFocus(int instance_id, bool focused) {
  if (focused) {
    focus_observed_ = true;
    if (focus_message_loop_runner_)
      focus_message_loop_runner_->Quit();
  } else {
    blur_observed_ = true;
    if (blur_message_loop_runner_)
      blur_message_loop_runner_->Quit();
  }
  BrowserPluginGuest::OnSetFocus(instance_id, focused);
}

void TestBrowserPluginGuest::OnTakeFocus(bool reverse) {
  advance_focus_observed_ = true;
  if (advance_focus_message_loop_runner_)
    advance_focus_message_loop_runner_->Quit();
  BrowserPluginGuest::OnTakeFocus(reverse);
}

void TestBrowserPluginGuest::DidStopLoading(
    RenderViewHost* render_view_host) {
  BrowserPluginGuest::DidStopLoading(render_view_host);
  load_stop_observed_ = true;
  if (load_stop_message_loop_runner_)
    load_stop_message_loop_runner_->Quit();
}

void TestBrowserPluginGuest::OnImeCancelComposition() {
  if (!ime_cancel_observed_) {
    ime_cancel_observed_ = true;
    if (ime_cancel_message_loop_runner_)
      ime_cancel_message_loop_runner_->Quit();
  }
  BrowserPluginGuest::OnImeCancelComposition();
}

void TestBrowserPluginGuest::OnResizeGuest(
    int instance_id,
    const BrowserPluginHostMsg_ResizeGuest_Params& params) {
  last_size_observed_in_resize_ = params.view_rect.size();
  if (last_size_observed_in_resize_ == expected_view_size_in_resize_ &&
      resize_guest_message_loop_runner_) {
    resize_guest_message_loop_runner_->Quit();
  }

  BrowserPluginGuest::OnResizeGuest(instance_id, params);
}

}  // namespace content