#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis

sorder = sorted([20,1,9,-12,100,10])
print(sorder)

#key函数来实现自定义的排序
sorderByKey = sorted([20,1,9,2,-12,299],key=abs)
print(sorderByKey)

#字符串排序
sortStr = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(sortStr)

#逆向排序
sortStrReverse = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True)
print(sortStrReverse)