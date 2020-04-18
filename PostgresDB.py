# coding: utf8

import sys
import psycopg2
import functions as help

#   Класс работы с БД Postgres на VDI
#   IPv4: 194.67.92.75
#   IPv6: 2A00:F940:2:1:2:0:0:1DEA

class PostgreSqlDB:   

    __conn = psycopg2.connect(  host = "194.67.92.75",  database = "avito",
                                user = "imacbot",       password = "Postgresql3881730@" )    
    
    def __commit(self):
        self.__conn.commit()

    def __del__(self):
        self.__conn.close()

    def isNewIMacByHash (self, hash):
        try:
            cursor = self.__conn.cursor()  
            cursor.execute( 'SELECT * FROM avito."T_MAC" WHERE "HASH" = %s', (hash,))                        
            return True if cursor.rowcount == 0 else False
        except Exception as error:
            print("Error during isNewIMac request {0}".format(error) )
        return False

    def isNewIMacByTitle (self, title, url):
            hash = help.getHash(title,url)
            return self.isNewIMacByHash(hash)

    
    def addNewIMac (self, mac):
        try:
            cursor = self.__conn.cursor()            
            cursor.execute('INSERT INTO avito."T_MAC" ("TITLE","LINK","HASH") VALUES(%s,%s,%s)',(mac['title'],mac['href'],mac['hash']))
            self.__commit()
        except Exception as error:
            print ("Error during addNewIMac execution : {0}".format(error))      

    
    def delMacByHash(self, hash):
        try:
            cursor = self.__conn.cursor()
            rez = cursor.execute('DELETE FROM avito."T_MAC" WHERE HASH=%s',(hash,))
            self.__commit()
            return True if rez.rowcount > 0 else False
        except Exception as error:
            print ("Error during addNewIMac execution : {0}".format(error))
        
        return False
    
    
    def delMac(self, title, url):
        try:
            cursor = self.__conn.cursor()
            rez = cursor.execute('DELETE FROM avito."T_MAC" WHERE "TITLE"=%s AND "LINK"=%s',(title,url))
            self.__commit()
            return True if rez.rowcount > 0 else False
        except Exception as error:
            print ("Error during addNewIMac execution : {0}".format(error))
        
        return False

    
    def delAllMac(self):
        try:
            cursor = self.__conn.cursor()
            rez = cursor.execute('DELETE FROM avito."T_MAC"')
            self.__commit()
            return True if rez.rowcount > 0 else False
        except Exception as error:
            print ("Error during addNewIMac execution : {0}".format(error))       

        return False