# coding: utf8

import sys
import functions as help
from bs4 import BeautifulSoup
import requests as req
from random import choice

class Avito:
    __url_imac27 = "https://www.avito.ru/moskva/nastolnye_kompyutery?pmax=50000&pmin=10000&s=104&q=imac+27"

    __agents__ = open('useragents.txt').read().split('\n')

    def findMacs(self):

        agent = choice(self.__agents__)        
        url = self.__url_imac27
        content = req.get(url,headers={'User-Agent': agent})
        
        print("connecting to {0}".format(url))
        print("agent {0}".format(agent))
        print("status {0}".format(content.status_code))        

        soap = BeautifulSoup(content.text, 'html.parser')
        tags = soap.find_all(attrs={"class":"snippet-link"})
        return self.__getImacsFromHTML(tags)


    def __getImacsFromHTML(self, tegs):
        macs = []
        for elem in tegs:
            try:        
                title = elem.attrs['title']
                href  = elem.attrs['href'] 
                hash  = help.getHash(title, href)                       
                macs.append({'title':title,'href':href,'hash':hash})
            except:
                continue
        return macs