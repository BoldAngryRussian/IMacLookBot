# coding: utf8

import sys
import Avito
import PostgresDB as dbPostgres
import DataBase as dbLite
import telegram as bot
import schedule
import time

class Service:

    __dbSQLite      = dbLite.SQLite() # локальная БД
    __dbPostgres    = dbPostgres.PostgreSqlDB() # реальная БД на VDI
    __avito         = Avito.Avito()
    __bot           = bot.TelegramBot()

    def plan(self):
        schedule.every(3).minutes.do(self.start)

    def start(self):        
        for mac in self.__avito.findMacs():
            print ("Checking url    {0}".format(mac['href']))
            if self.__dbPostgres.isNewIMacByHash(mac['hash']):
                print ("New add title   {0}".format(mac['title']))                
                self.__dbPostgres.addNewIMac(mac)                
                self.__bot.Send(  '{0}+http://avito.ru{1}'.format(mac['title'],mac['href']) )

if __name__ == "__main__":    
    print ("---- Telegram bot ImacLooking started ----")        
    Service().plan()
    while 1:
        schedule.run_pending()
        time.sleep(1)        