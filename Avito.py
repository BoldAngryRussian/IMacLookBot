import sys
import functions as help
from bs4 import BeautifulSoup
import requests as req

class Avito:
    __url_imac27 = "https://www.avito.ru/moskva/nastolnye_kompyutery?pmax=50000&pmin=10000&s=104&q=imac+27"

    def findMacs(self):
        content = req.get(self.__url_imac27)
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