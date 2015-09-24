#!/usr/bin/env python3
# -*- coding:utf-8 -*-

age = 20
print('your age is',age)
if age >= 6:
	print('teenager')
elif age > 18:
	print('adult')
else:
	print('kid')

s = input('input your age:')
birth = int(s)
if birth < 2000:
	print('00前')
else:
	print('00后')