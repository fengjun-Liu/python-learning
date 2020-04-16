import requests
from bs4 import BeautifulSoup

conurl='http://www.ngchina.com.cn/photography/photo_of_the_day/6260.html'

con=requests.get(conurl)
consoup=BeautifulSoup(con.content,'lxml')
url=consoup.find('div',{"class":"content js_content"}).div.div.div.ul.li.a.img['src']
print(url)