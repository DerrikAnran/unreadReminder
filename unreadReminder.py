#Filename:unreadReminder.py
#-*- coding:utf-8 -*-

'''
unreadReminder.py
------------

这是一个将我的微信头像右上角加上红色数字，
来表示类似提示有未读信息数量的提示效果
Author:曾安然
制作时间：2017年6月9日

------------

'''
import Image, ImageDraw, ImageFont, ImageFilter
import random

#随机消息数字
def rndNumber():
    return str(random.randint(1, 99))

#打开头像文件:
im = Image.open(r'C:\Users\apple\Documents\PYpractice\icon.jpg')
#得到图像尺寸：
width, height = im.size
#创建font字体对象给ImageDraw中的text函数使用，选择数字字体和大小
font1 = ImageFont.truetype('Arial.ttf',58)
#创建draw对象，对icon.jpg操作
draw = ImageDraw.Draw(im)
number = rndNumber()
#利用ink函数将画笔默认的白色改为红色
draw.ink = 255 + 0 * 256 + 0 * 256 * 256
#利用text函数添加number到图片中去
draw.text([0.9*width,0.05*height], number, font = font1)
#将添加数字后的图片保存
im.save(r'C:\Users\apple\Documents\PYpractice\icon1.jpg', 'jpeg')
