#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis


print('abs:',abs(-100))
print('max:',max(1,2,5,7,12,8))

print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

a = abs
print(a(-1))

#自定义函数

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>0:
		return x
	else:
		return -x

print('user define function my_abs:',my_abs(-12))
#print('user define function my_abs raise TypeError:',my_abs('a'))


#返回多个值
print('====返回多个值例子====')
import math
def move(x,y,step,angle = 0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx,ny
print('表达式x, y = move(100, 100, 60, math.pi / 6)返回多个值','=',move(100, 100, 60, math.pi / 6))
r = move(100, 100, 60, math.pi / 6)
print('返回单一值:', r)

#
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。
#