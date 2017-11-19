# coding=utf-8
import numpy
import itchat
import os,jieba
import PIL.Image as Image
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt


def w_c(list,name):
    # 将字符串切割
    wordlist_jieba = jieba.cut(list,cut_all=False)
    print(type(wordlist_jieba))
    # 以“ ”word的格式生成一个字符串给WordCloud提供处理
    wl_space_split = " ".join(wordlist_jieba)
    # 图片尽量为区别较大的，可以转为二值化的图片
    ping_mask = numpy.array(Image.open("C:\\Users\cello\Desktop\pthon包\word_cloud-master\word_cloud-master\examples\\alice_color.png"))
    print(ping_mask)
    # 进行word的词云组合
    my_word_cloud = WordCloud(mask=ping_mask, width=900, height=506,background_color="white", scale=1,max_words=2000, max_font_size=400, random_state=42,
                              font_path="C:\Windows\Fonts\msyhbd.ttf").generate(wl_space_split)
    # IImageColorGenerator 抽取图片的对应色彩度
    image_colors=ImageColorGenerator(ping_mask)
    # 按抽取的色彩度来显示图片
    plt.imshow(my_word_cloud.recolor(color_func=image_colors))
    plt.imshow(my_word_cloud)
    plt.axis("off")
    plt.show()
    my_word_cloud.to_file(os.path.join("%s.jpg"%name))
    return name+".jpg"

# 登入python版微信
itchat.auto_login(enableCmdQR=False)
# 获取好友信息列表
friends = itchat.get_friends(update=True)
user = friends[0]["UserName"]
print(user)
nick_name_list = []
my_signature_list = []
gender = []
# 逐个提取好友相关信息
for i in friends:
    friends_nick_name = i["NickName"]  # 昵称
    if friends_nick_name == "''" or "'\\'" in friends_nick_name or "emoji" in friends_nick_name:  # 去掉一些表情，以及不规则字符
        pass
    else:
        nick_name_list.append(friends_nick_name)
    signature = i["Signature"]  # 个性签名
    if  signature == "''"or "'\\'" in signature or "emoji" in signature:  # 去掉一些表情，以及不规则字符
        pass
    else:
        my_signature_list.append(signature)
    gender.append(i["Sex"])
    memberlist = i["MemberList"]
my_signature_str = " ".join(my_signature_list)
nick_name_str = " ".join(nick_name_list)
p1 = w_c(my_signature_str,"signature")
print(p1)
itchat.send_image(p1,"filehelper")
p2 = w_c(nick_name_str,"nick_name")
itchat.send_image(p2,"filehelper")
print(gender)
itchat.send_msg("男生有%s,女生有%s"%(gender.count(1),gender.count(2)),"filehelper")

