# -*- coding: utf-8 -*-

import os
import zipfile
from urllib.request import urlretrieve
#from bs4 import BeautifulSoup

def get_page_source(url):
        
    zip_file =os.path.join('/home/joelrj/eclipse-workspace/Zerodha/','zipfile.tar.gz')
    urlretrieve(url,zip_file) 
    print ("downloaded")
    zip_extract = zipfile.ZipFile('/home/joelrj/eclipse-workspace/Zerodha/zipfile.tar.gz', 'r')
    zip_extract.extractall('/home/joelrj/eclipse-workspace/Zerodha/')
    zip_extract.close()
    return ("extracted")

url = 'https://www.bseindia.com/download/BhavCopy/Equity/EQ080318_CSV.ZIP'
print(get_page_source(url))
