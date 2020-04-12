# coding: utf8

import sys
import Avito
import DataBase as db
import telegram as bot

class Service:
    __db    = db.SQLite()
    __avito = Avito.Avito()
    __bot   = bot.TelegramBot()
    def start(self):
        for mac in self.__avito.findMacs():
            if self.__db.isNewIMacByHash(mac['hash']):
                #   Найдено новое объявление. Добавляем его в БД
                self.__db.addNewIMac(mac)
                #   Отсылаем уведомление в телеграмм                
                self.__bot.Send(  '{0}+http://avito.ru{1}'.format(mac['title'],mac['href']) )


if __name__ == "__main__":
    print ("---- Telegram bot ImacLooking started ----")
    Service().start()
    print("---- finished ----")
