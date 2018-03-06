#coding:utf-8
from PIL import Image,ImageFilter

im=Image.open('test.jpg')

#获得图像尺寸
w,h=im.size
print '图像的原始尺寸为:%s--%s'%(w,h)

#缩放到50%
im.thumbnail((w//2,h//2))
print '缩放后图像尺寸为:%s--%s'%(w//2,h//2)

#把缩放后的图像用jpeg格式保存
im.save('thumbnail.jpg','jpeg')

#应用模糊滤镜
im2=im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')
