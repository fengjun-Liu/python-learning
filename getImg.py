import requests
import os
url ='http://www.ngchina.com.cn/photography/photo_of_the_day/'
url ='http://image.ngchina.com.cn/2020/0316/20200316124042110.jpg'
root="D://pics//"
path=root+url.split("/")[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path)
		r=requests.get(url)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print("文件保存成功")
	else：
		print("文件已存在")
except:
	print("爬取失败")