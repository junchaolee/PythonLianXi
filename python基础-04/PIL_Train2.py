#coding:utf-8
from PIL import Image,ImageDraw,ImageFont,ImageFilter

import random

#随机字母
def rndChar():
    return chr(random.randint(65,90))

#随机颜色
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#随机颜色2
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

#240*60
width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))

#创建Font对象
font=ImageFont.truetype('simhei.ttf',36)

#创建Draw对象
draw=ImageDraw.Draw(image)

#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())

#输出文字
for t in range(4):
    z=rndChar()
    draw.text((60*t+10,10),z,font=font,fill=rndColor2())
    print z,

#模糊并保存图像
im=image.filter(ImageFilter.BLUR)
im.save('code.jpg','jpeg')