// Copyright 2013 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "components/dom_distiller/core/fake_distiller.h"

#include "base/auto_reset.h"
#include "base/bind.h"
#include "base/message_loop/message_loop.h"
#include "testing/gtest/include/gtest/gtest.h"

namespace dom_distiller {
namespace test {

MockDistillerFactory::MockDistillerFactory() {}
MockDistillerFactory::~MockDistillerFactory() {}

FakeDistiller::FakeDistiller(bool execute_callback)
    : execute_callback_(execute_callback),
      destruction_allowed_(true) {
  EXPECT_CALL(*this, Die()).Times(testing::AnyNumber());
}

FakeDistiller::~FakeDistiller() {
  EXPECT_TRUE(destruction_allowed_);
  Die();
}

void FakeDistiller::DistillPage(
    const GURL& url,
    scoped_ptr<DistillerPage> distiller_page,
    const DistillationFinishedCallback& article_callback,
    const DistillationUpdateCallback& page_callback) {
  url_ = url;
  article_callback_ = article_callback;
  page_callback_ = page_callback;
  if (execute_callback_) {
    scoped_ptr<DistilledArticleProto> proto(new DistilledArticleProto);
    proto->add_pages()->set_url(url_.spec());
    PostDistillerCallback(proto.Pass());
  }
}

void FakeDistiller::RunDistillerCallback(
    scoped_ptr<DistilledArticleProto> proto) {
  ASSERT_FALSE(execute_callback_) << "Cannot explicitly run the distiller "
                                     "callback for a fake distiller created "
                                     "with automatic callback execution.";
  PostDistillerCallback(proto.Pass());
}

void FakeDistiller::PostDistillerCallback(
    scoped_ptr<DistilledArticleProto> proto) {
  base::MessageLoop::current()->PostTask(
      FROM_HERE,
      base::Bind(&FakeDistiller::RunDistillerCallbackInternal,
                 base::Unretained(this),
                 base::Passed(&proto)));
}

void FakeDistiller::RunDistillerCallbackInternal(
    scoped_ptr<DistilledArticleProto> proto) {
  EXPECT_FALSE(article_callback_.is_null());

  base::AutoReset<bool> dont_delete_this_in_callback(&destruction_allowed_,
                                                     false);
  article_callback_.Run(proto.Pass());
  article_callback_.Reset();
}

}  // namespace test
}  // namespace dom_distiller
