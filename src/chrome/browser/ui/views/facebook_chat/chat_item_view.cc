// BitPop browser with features like Facebook chat and uncensored browsing. 
// Copyright (C) 2014 BitPop AS
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

#include "chrome/browser/ui/views/facebook_chat/chat_item_view.h"

#include <string>

#include "base/location.h"
#include "base/string_number_conversions.h"
#include "base/string_util.h"
#include "base/utf_string_conversions.h"
#include "chrome/browser/facebook_chat/facebook_chat_manager.h"
#include "chrome/browser/facebook_chat/facebook_chat_manager_service_factory.h"
#include "chrome/browser/profiles/profile.h"
#include "chrome/browser/themes/theme_service.h"
#include "chrome/browser/ui/browser.h"
#include "chrome/browser/ui/browser_window.h"
#include "chrome/browser/ui/lion_badge_image_source.h"
#include "chrome/browser/ui/views/facebook_chat/chatbar_view.h"
#include "chrome/browser/ui/views/facebook_chat/chat_notification_popup.h"
#include "chrome/browser/ui/views/frame/browser_view.h"
#include "chrome/browser/ui/views/infobars/infobar_button_border.h"
#include "chrome/common/badge_util.h"
#include "chrome/common/url_constants.h"
#include "googleurl/src/gurl.h"
#include "googleurl/src/url_util.h"
#include "grit/generated_resources.h"
#include "grit/theme_resources.h"
#include "grit/ui_resources.h"
#include "third_party/skia/include/core/SkBitmap.h"
#include "third_party/skia/include/core/SkPaint.h"
#include "third_party/skia/include/core/SkTypeface.h"
#include "third_party/skia/include/effects/SkGradientShader.h"
#include "ui/base/resource/resource_bundle.h"
#include "ui/gfx/canvas.h"
#include "ui/gfx/skia_util.h"
#include "ui/views/background.h"
#include "ui/views/controls/button/image_button.h"
#include "ui/views/controls/button/text_button.h"
#include "ui/views/controls/label.h"

using views::CustomButton;
using views::Label;
using views::View;

namespace {

const gfx::Size kChatButtonSize = gfx::Size(158, 25);

const int kCloseButtonPadding = 3;

const int kNotificationMessageDelaySec = 10;

const int kNotifyIconDimX = 26;
const int kNotifyIconDimY = 15;

const int kTextRightPadding = 13;
}

class OverOutTextButton : public views::TextButton {
public:
  OverOutTextButton(ChatItemView* owner, const std::wstring& text)
    : views::TextButton(owner, text),
      owner_(owner) {
  }

  virtual void OnMouseEntered(const ui::MouseEvent& event) OVERRIDE {
    owner_->OnMouseEntered(event);
  }

  virtual void OnMouseExited(const ui::MouseEvent& event) OVERRIDE {
    owner_->OnMouseExited(event);
  }
protected:
  virtual gfx::Rect GetTextBounds() const OVERRIDE {
    DCHECK_EQ(alignment_, ALIGN_LEFT);
	DCHECK_EQ(icon_placement(), views::TextButton::ICON_ON_LEFT);
    gfx::Insets insets = GetInsets();
    int content_width = width() - insets.right() - insets.left();
    int extra_width = 0;

    const gfx::ImageSkia& icon = GetImageToPaint();
    if (icon.width() > 0)
      extra_width = icon.width() + (text_.empty() ? 0 : icon_text_spacing());
    content_width -= extra_width;

    gfx::Rect bounds = TextButton::GetTextBounds();
    bounds.set_width(content_width - kTextRightPadding);

    return bounds;
  }

private:
  ChatItemView *owner_;
};

ChatItemView::ChatItemView(FacebookChatItem *model, ChatbarView *chatbar)
  : model_(model),
    chatbar_(chatbar),
    close_button_bg_color_(0),
    chat_popup_(NULL),
    notification_popup_(NULL),
    isMouseOverNotification_(false),
    notification_icon_(NULL) {

  model->AddObserver(this);

  ResourceBundle& rb = ResourceBundle::GetSharedInstance();

  openChatButton_ = new OverOutTextButton(this, UTF8ToWide(model->username()));
  //openChatButton_->SetNormalHasBorder(true);
  openChatButton_->set_icon_placement(views::TextButton::ICON_ON_LEFT);
  openChatButton_->set_border(new InfoBarButtonBorder);
  //openChatButton_->SetNormalHasBorder(true);
  openChatButton_->SetAnimationDuration(0);
  openChatButton_->SetEnabledColor(SK_ColorBLACK);
  openChatButton_->SetDisabledColor(SK_ColorBLACK);
  openChatButton_->SetHighlightColor(SK_ColorBLACK);
  openChatButton_->SetHoverColor(SK_ColorBLACK);
  openChatButton_->SetFont(rb.GetFont(ResourceBundle::BaseFont));

  StatusChanged();  // sets button icon
  AddChildView(openChatButton_);

  // Add the Close Button.
  close_button_ = new views::ImageButton(this);
  close_button_->SetImage(views::CustomButton::STATE_NORMAL,
                          rb.GetImageSkiaNamed(IDR_TAB_CLOSE));
  close_button_->SetImage(views::CustomButton::STATE_HOVERED,
                          rb.GetImageSkiaNamed(IDR_TAB_CLOSE_H));
  close_button_->SetImage(views::CustomButton::STATE_PRESSED,
                          rb.GetImageSkiaNamed(IDR_TAB_CLOSE_P));
  //close_button_->SetTooltipText(
  //    UTF16ToWide(l10n_util::GetStringUTF16(IDS_TOOLTIP_CLOSE_TAB)));
  //close_button_->SetAccessibleName(
  //    l10n_util::GetStringUTF16(IDS_ACCNAME_CLOSE));
  // Disable animation so that the red danger sign shows up immediately
  // to help avoid mis-clicks.
  close_button_->SetAnimationDuration(0);
  AddChildView(close_button_);
}

ChatItemView::~ChatItemView() {
  if (model_)
    model_->RemoveObserver(this);
  if (close_button_)
    delete close_button_;
  if (openChatButton_)
    delete openChatButton_;
  if (chat_popup_) {
    //chat_popup_->GetWidget()->RemoveObserver(this);
    //chat_popup_->GetWidget()->Close();
    //delete chat_popup_;
    chat_popup_->GetWidget()->Close();
  }
  if (notification_popup_) {
    notification_popup_->GetWidget()->RemoveObserver(this);
    notification_popup_->GetWidget()->Close();
    delete notification_popup_;
  }
  if (notification_icon_)
    delete notification_icon_;

  for (TimerList::iterator it = timers_.begin(); it != timers_.end(); it++) {
    if (*it && (*it)->IsRunning())
      (*it)->Stop();
    delete *it;
    *it = NULL;
  }
}

void ChatItemView::ButtonPressed(views::Button* sender, const ui::Event& event) {
  if (sender == close_button_) {
    Close(true);
  } else if (sender == openChatButton_) {
    if (!chat_popup_)
      ActivateChat();
  }
}

void ChatItemView::Layout() {
  gfx::Rect bounds;
  bounds.set_x(0);
  bounds.set_y(0);
  gfx::Size sz = GetPreferredSize();
  bounds.set_size(sz);

  openChatButton_->SetBoundsRect(bounds);

  gfx::Size closeButtonSize = close_button_->GetPreferredSize();
  close_button_->SetBounds(bounds.width() - closeButtonSize.width() - kCloseButtonPadding,
                            bounds.height() / 2 - closeButtonSize.height() / 2,
                            closeButtonSize.width(),
                            closeButtonSize.height());

  if (notification_popup_) {
    // For the call to SizeToContents() to be made
    notification_popup_->SetAlignment(views::BubbleBorder::ALIGN_ARROW_TO_MID_ANCHOR);
  }

  if (chat_popup_) {
    // For the call to SizeToContents() to be made
    chat_popup_->SetAlignment(views::BubbleBorder::ALIGN_ARROW_TO_MID_ANCHOR);
  }
}

gfx::Size ChatItemView::GetPreferredSize() {
  return kChatButtonSize;
}

void ChatItemView::OnChatUpdated(FacebookChatItem *source) {
  DCHECK(source == model_);
  switch (source->state()) {
  case FacebookChatItem::REMOVING:
    Close(false);
    break;
  case FacebookChatItem::NUM_NOTIFICATIONS_CHANGED:
    NotifyUnread();
    break;
  case FacebookChatItem::STATUS_CHANGED:
    StatusChanged();
    break;
  }
}

void ChatItemView::AnimationProgressed(const ui::Animation* animation) {
}

void ChatItemView::StatusChanged() {
  ResourceBundle& rb = ResourceBundle::GetSharedInstance();
  if (model_->num_notifications() == 0) {
    if (model_->status() == FacebookChatItem::AVAILABLE)
      openChatButton_->SetIcon(*rb.GetImageSkiaNamed(IDR_FACEBOOK_ONLINE_ICON_14));
    else if (model_->status() == FacebookChatItem::IDLE)
      openChatButton_->SetIcon(*rb.GetImageSkiaNamed(IDR_FACEBOOK_IDLE_ICON_14));
    else
      openChatButton_->SetIcon(gfx::ImageSkia::ImageSkia());
  } else if (model_->status() != FacebookChatItem::COMPOSING)
    UpdateNotificationIcon();

  if (model_->status() == FacebookChatItem::COMPOSING)
    openChatButton_->SetIcon(*rb.GetImageSkiaNamed(IDR_FACEBOOK_COMPOSING_ICON_14));
}

void ChatItemView::Close(bool should_animate) {
  if (notification_popup_)
    notification_popup_->GetWidget()->Close();
  chatbar_->Remove(this, should_animate);
}

void ChatItemView::OnPaint(gfx::Canvas* canvas) {
  views::View::OnPaint(canvas);

  ResourceBundle &rb = ResourceBundle::GetSharedInstance();
  SkColor bgColor = GetThemeProvider()->GetColor(ThemeService::COLOR_TAB_TEXT);

  if (bgColor != close_button_bg_color_) {
    close_button_bg_color_ = bgColor;
    close_button_->SetBackground(close_button_bg_color_,
        rb.GetImageSkiaNamed(IDR_TAB_CLOSE),
        rb.GetImageSkiaNamed(IDR_TAB_CLOSE_MASK));
  }
}

void ChatItemView::ActivateChat() {
  if (notification_popup_)
      notification_popup_->GetWidget()->Close();

  model_->ClearUnreadMessages();
  StatusChanged();  // restore status icon
  SchedulePaint();

  FacebookChatManager* mgr = FacebookChatManagerServiceFactory::GetForProfile(chatbar_->browser()->profile());

  if (mgr) {
    // open popup
    std::string urlString(chrome::kFacebookChatExtensionPrefixURL);
    urlString += chrome::kFacebookChatExtensionChatPage;
    urlString += "#?friend_jid=";
    urlString += model_->jid() + "&jid=" + mgr->global_my_uid();
    urlString += "&name=";
    url_canon::RawCanonOutput<1024> out;
    url_util::EncodeURIComponent(
                    model_->username().c_str(),
                    model_->username().length(),
                    &out);
    urlString += std::string(out.data(), out.length());

    chat_popup_ = ExtensionChatPopup::ShowPopup(GURL(urlString), chatbar_->browser(),
                                  this, BubbleBorder::BOTTOM_CENTER);
    chat_popup_->GetWidget()->AddObserver(this);
    openChatButton_->SetEnabled(false);
  }
}

const FacebookChatItem* ChatItemView::GetModel() const {
  return model_;
}

void ChatItemView::OnWidgetClosing(views::Widget* bubble) {
  if (chat_popup_ && bubble == chat_popup_->GetWidget()) {
    bubble->RemoveObserver(this);
    chat_popup_ = NULL;
    openChatButton_->SetEnabled(true);
  }

  if (notification_popup_ && bubble == notification_popup_->GetWidget()) {
    bubble->RemoveObserver(this);
    notification_popup_ = NULL;

    for (TimerList::iterator it = timers_.begin(); it != timers_.end(); it++) {
      if (*it && (*it)->IsRunning())
        (*it)->Stop();
    }
  }
}

void ChatItemView::NotifyUnread() {
  if (model_->num_notifications() > 0) {
    if (!notification_popup_) {
      notification_popup_ = ChatNotificationPopup::Show(this, BubbleBorder::BOTTOM_CENTER);
      notification_popup_->GetWidget()->AddObserver(this);
    }

    notification_popup_->PushMessage(model_->GetMessageAtIndex(model_->num_notifications() - 1));

    ChatTimer *timer = NULL;
    for (TimerList::iterator it = timers_.begin(); it != timers_.end(); it++) {
      if (!(*it)->IsRunning()) {
        timer = *it;
        break;
      }
    }
    if (timer == NULL) {
      timer = new ChatTimer();
      timers_.push_back(timer);
    }
    timer->Start(FROM_HERE, base::TimeDelta::FromSeconds(kNotificationMessageDelaySec), this, &ChatItemView::TimerFired);

    if (!visible())
      chatbar_->PlaceFirstInOrder(this);

    UpdateNotificationIcon();
    openChatButton_->SchedulePaint();
  }
}

void ChatItemView::TimerFired() {
  if (notification_popup_)
    (void)notification_popup_->PopMessage();
}

gfx::Rect ChatItemView::RectForChatPopup() {
  View* reference_view = openChatButton_;
  gfx::Point origin;
  View::ConvertPointToScreen(reference_view, &origin);
  gfx::Rect rect = reference_view->bounds();
  rect.set_origin(origin);

  return rect;
}

gfx::Rect ChatItemView::RectForNotificationPopup() {
  View* reference_view = openChatButton_;
  gfx::Point origin;
  View::ConvertPointToScreen(reference_view, &origin);
  gfx::Rect rect = reference_view->bounds();
  rect.set_origin(origin);
  rect.set_width(20);

  return rect;
}

void ChatItemView::OnMouseEntered(const ui::MouseEvent& event) {
  if (!notification_popup_ && model_->num_notifications() > 0) {

    notification_popup_ = ChatNotificationPopup::Show(this, BubbleBorder::BOTTOM_CENTER);
    notification_popup_->GetWidget()->AddObserver(this);
    notification_popup_->PushMessage(model_->GetMessageAtIndex(model_->num_notifications() - 1));
    isMouseOverNotification_ = true;
  }
}

void ChatItemView::OnMouseExited(const ui::MouseEvent& event) {
  if (isMouseOverNotification_ && notification_popup_) {
    //notification_popup_->set_fade_away_on_close(false);
    notification_popup_->GetWidget()->Close();
  }
}

int ChatItemView::GetRightOffsetForText() const {
  return close_button_->width() + 2 * kCloseButtonPadding;
}

void ChatItemView::UpdateNotificationIcon() {
  if (notification_icon_) {
    delete notification_icon_;
    notification_icon_ = NULL;
  }

  int number = model_->num_notifications();
  if (number > 0) {
    if (number > 99)
      number = 99;
    std::string num = base::IntToString(number);

    LionBadgeImageSource* source = new LionBadgeImageSource(
            gfx::Size(kNotifyIconDimX, kNotifyIconDimY),
            num);

    openChatButton_->SetIcon(gfx::ImageSkia(source, source->size()));
  }
}