#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis
# 获取对象信息

#type()判断对象类型
print(type(123))

#判断函数 使用types模块中定义的常量
import types
def fn():
	pass

b = type(fn) == types.FunctionType
print(b)

#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
import Extends
a = Extends.Animal()
d = Extends.Dog()
c = Extends.Cat()
print(isinstance(a,Extends.Animal))
print(isinstance(d,Extends.Dog))
print(isinstance(c,Extends.Cat))

#dir()获取对象所有方法属性
print(dir(a))

#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
	"""docstring for MyObject"""
	def __init__(self, arg):
		super(MyObject, self).__init__()
		self.arg = arg
	def power(self):
		return self.arg * self.arg

obj = MyObject('aa')
b = hasattr(obj,'arg') #判断是否有属性 'arg'?
print(b)

setattr(obj,'arg',12)

print(getattr(obj,'arg'))
