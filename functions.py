import sys
import hashlib

def getHash(title, url):
    return hashlib.md5((title + url).encode('utf-8')).hexdigest()