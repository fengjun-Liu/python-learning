import requests

imgurl="http://img0.dili360.com/ga/M02/02/18/wKgBzFQ2x9eAbZn8AATCSQolols997.jpg@!rw17"
file_att = 'image_tmp.jpg'

imgre = requests.get(imgurl)
open(file_att, "wb").write(imgre.content)
print("下载完毕")


# f = open('cat_500_600.jpg','wb')

# try:
	# data = f.write(imgre.content)

# finally:
	# f.close()