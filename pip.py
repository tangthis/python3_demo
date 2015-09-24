#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis

#安装第三方模块，使用pip命令


#示例：图片裁剪 Pillow
#安装 pip install Pillow
#生成缩略图
from PIL import Image
im = Image.open('D:\\test.png')
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('thumb.jpg','JPEG')
