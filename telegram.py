# coding: utf8

import sys
import requests as req

class TelegramBot:
    __token = "1109530539:AAHPznPnE7j0wpesWD4Fqyiy1qetkJUDbbw"
    __chat  = "-462298978"
    __url   = "https://api.telegram.org/bot$TOKEN/sendMessage?chat_id=$CHAT_ID&text=Hello+World"
    __send  = "https://api.telegram.org/bot1109530539:AAHPznPnE7j0wpesWD4Fqyiy1qetkJUDbbw/sendMessage?chat_id=-462298978&text="

    def Send(self, text):
        req.post(self.__send + text)