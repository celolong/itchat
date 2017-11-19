from numpy import *
import itchat
import urllib
import requests
import os
import PIL.Image as Image
from os import listdir
import math

# 登入python版微信
itchat.auto_login(enableCmdQR=False)
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]
user = friends[0]["UserName"]
print(user)
num = 0
os.mkdir(user)
# 获取好友头像列表并下载
for i in friends:
    img = itchat.get_head_img(userName=i["UserName"])
    fileImage = open(user + "/" + str(num) + ".jpg","wb")
    fileImage.write(img)
    fileImage.close()
    num +=1
# 创建一个
pics = listdir(user)
# 总共有多少图片
numPic = len(pics)
print(numPic)
# 计算合成一张图片后的边长，默认正方形
eachsize = int(math.sqrt(float(640*640) / numPic))
numline = int(640 / eachsize)

toImage = Image.new('RGB', (640, 640))
print(numline)

x = 0
y = 0

for i in pics:
    try:
        # 打开图片
        img= Image.open(user + "/" +i)
    except IOError:
        print("Erro:没有找到文件获取文件失败")
    else:
        img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
        # 拼接图片
        toImage.paste(img, (x * eachsize, y * eachsize))
        x += 1
        if x == numline:
            x = 0
            y += 1
# 保存图片到本地
toImage.save(user + ".jpg")
# 在微信的文件传输助手发合成后的图片给使用者：
itchat.send_image(user + ".jpg", 'filehelper')