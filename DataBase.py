# coding: utf8

import sys
import sqlite3
import functions as help

class SQLite:    
    #   Строка соединения с БД
    __db_url = "avito.db"    
    #   Объект соединнеия с БД
    __conn = sqlite3.connect(__db_url)    
    #   проверка новое ли объявление или нет
    def __commit(self):
        self.__conn.commit()

    def __del__(self):
        self.__conn.close()

    def isNewIMacByHash (self, hash):
        try:
            cursor = self.__conn.cursor()            
            if len(list(cursor.execute( 'SELECT * FROM T_IMAC WHERE HASH=?', (hash,)))) == 0:
                return True
        except Exception as error:
            print("Error during isNewIMac request {0}".format(error) )
        return False

    def isNewIMacByTitle (self, title, url):
            hash = help.getHash(title,url)
            return self.isNewIMacByHash(hash)

    #   Добавление новой записи об объявлении
    def addNewIMac (self, mac):
        try:
            cursor = self.__conn.cursor()            
            cursor.execute("INSERT OR IGNORE INTO T_IMAC (TITLE,LINK,HASH) VALUES(?,?,?)",(mac['title'],mac['href'],mac['hash']))
            self.__commit()
        except Exception as error:
            print ("Error during addNewIMac execution : {0}".format(error))      

    #   Удаление записи об объявлении по хешу
    def delMacByHash(self, hash):
        try:
            cursor = self.__conn.cursor()
            rez = cursor.execute("DELETE FROM T_IMAC WHERE HASH=?",(hash,))
            self.__commit()
            return True if rez.rowcount > 0 else False
        except Exception as error:
            print ("Error during addNewIMac execution : {0}".format(error))
        
        return False
    
    #   Удаление записи об объявлении по названию и url
    def delMac(self, title, url):
        try:
            cursor = self.__conn.cursor()
            rez = cursor.execute("DELETE FROM T_IMAC WHERE TITLE=? AND LINK=?",(title,url))
            self.__commit()
            return True if rez.rowcount > 0 else False
        except Exception as error:
            print ("Error during addNewIMac execution : {0}".format(error))
        
        return False

    #   Удаление записи об объявлении по названию и url
    def delAllMac(self):
        try:
            cursor = self.__conn.cursor()
            rez = cursor.execute("DELETE FROM T_IMAC")
            self.__commit()
            return True if rez.rowcount > 0 else False
        except Exception as error:
            print ("Error during addNewIMac execution : {0}".format(error))       

        return False
