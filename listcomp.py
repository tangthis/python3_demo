#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis

lr = list(range(1,11))
print(lr)

lr1 = [x * x for x in range(1,20) if x % 2 == 0]
print(lr1)

lr3 = [m + n for m in 'ABC' for n in 'XYZ']
print(lr3)

#列出目录文件名
print('列出目录文件名')
import os # 导入os模块
lr4 = [x for x in os.listdir('.')] # os.listdir可以列出文件和目录
print(lr4)