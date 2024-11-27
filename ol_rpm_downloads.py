import requests
import bs4
import json
import re

url='https://yum.oracle.com/repo/OracleLinux/OL9/baseos/latest/x86_64/index.html'

def download_url(url):
    r=requests.get(url)
    if(r.status_code != 200):
        return False
    if('text/html' in r.headers['Content-Type']):
        ol_web = r.text
        webparsing(ol_web)
        return 'Webparsing is done - check Linux_rpm list'
    else:
        return 'Given url is not a webpage content'


Linux_rpm=[]
def webparsing(webpage):
    print(webpage)
    ol_obj = bs4.BeautifulSoup(webpage)
    for var in ol_obj.find_all('a'):
        if(re.search('rpm$',var.get('href'))):
            Linux_rpm.append(var.string)


rv=download_url(url)
if(rv):
    print(rv)
else:
    print('url download is failed')
    
    

ol_rpm['OL9']=Linux_rpm # adding new data to an existing dict

# create a json file
wobj = open('E:\\ol.json','w')
json.dump(ol_rpm,wobj) 
wobj.close()


