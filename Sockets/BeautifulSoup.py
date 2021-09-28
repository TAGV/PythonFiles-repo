import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSl errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the URL ----  ")                     #Enter a complete URl : https://www.tennis.com/
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

#print(soup.prettify())
print(soup.title)
#print(soup.get_text)

#Scrap for href tags under the anchor tags: Extracts all the links on the website
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))

