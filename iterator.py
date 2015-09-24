#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis

#list iterator
d = ['1',2,'a','b']
for key in d:
	print(key)


#dict
d1 = {'a':1,'b':2,'c':3}
#dict key
for key in d1:
	print(key)

#dict values
for val in d1.values():
	print(val)

#dict items
for k,v in d1.items():
	print('k is %s,v is %s' % (k,v))
