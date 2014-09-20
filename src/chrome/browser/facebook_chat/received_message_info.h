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

#ifndef CHROME_BROWSER_FACEBOOK_CHAT_FACEBOOK_RECEIVED_MESSAGE_INFO_H_
#define CHROME_BROWSER_FACEBOOK_CHAT_FACEBOOK_RECEIVED_MESSAGE_INFO_H_

#pragma once

#include <string>

#include "base/memory/scoped_ptr.h"

struct FacebookChatCreateInfo;

struct ReceivedMessageInfo {
  ReceivedMessageInfo(const std::string &jid,
                         const std::string &username,
                         const std::string &status,
                         const std::string &message);
  ReceivedMessageInfo();
  ~ReceivedMessageInfo();

  scoped_ptr<FacebookChatCreateInfo> chatCreateInfo;
  std::string message;
};

#endif  // CHROME_BROWSER_FACEBOOK_CHAT_RECEIVED_MESSAGE_INFO_H_