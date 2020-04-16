import requests
from bs4 import BeautifulSoup
from datetime import datetime

#获取今日日期
dt=datetime.now()
datemd=dt.strftime("%Y/%m%d")

imgsurl='http://www.ngchina.com.cn/photography/photo_of_the_day/'

imgs=requests.get(imgsurl)
imgssoup=BeautifulSoup(imgs.content,'lxml')
#查找imgs类型的a
imgurls=imgssoup.findAll('a',{"class":"imgs"})

for imgurl in imgurls:
	if imgurl.img['src'].find(datemd)>0:
		conurl='http://www.ngchina.com.cn'+imgurl['href']
		print(conurl)
		print(imgurl.parent.div.h5.a.text)
		break
		
con=requests.get(conurl)
consoup=BeautifulSoup(con.content,'lxml')
url=consoup.find('div',{"class":"content js_content"}).div.div.div.ul.li.a.img['src']