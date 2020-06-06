from bs4 import BeautifulSoup
from requests import get
import pandas as pd
from tqdm import tqdm
from dateutil import parser
import string

# Checking for the total no. of pages

url = 'https://ekantipur.com/search/2020/विदेश'
base='https://ekantipur.com'
soup = BeautifulSoup(get(url).text, 'lxml')

containers=soup.findAll("article")
articles_count=len(containers)
put_to_file=""
for x in range(0,articles_count):
    titles=containers[x].select("h2")
    print(titles[0].text)
    put_to_file=put_to_file+titles[0].text+"\n"
    #link=containers[0].select("h2")
    #link=link.findAll(href=True)
    #print(link)
    
    link=containers[x].findAll("h2")
    link_url=link[0].findAll("a",href=True)
    link_url=base+ link_url[0]['href']
    print(link_url)
    
    
    inner_soup=BeautifulSoup(get(link_url).text, 'lxml')
    inner_container=inner_soup.find_all("div",{"class":"description"})
    desc=inner_container[0].find_all("p")
    for i in range (len(desc)):
        print(desc[i].text)
        put_to_file=put_to_file+ desc[i].text+"\n"
    
    print("-----------------------------------------------")
    put_to_file=put_to_file+ "-----------------------------------------------"+"\n"


fp=open("kala.txt","wb")
put_to_file = fp.write(bytes(put_to_file.encode('utf-8')))
fp.close()
