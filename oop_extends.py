#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis
# 面向对象（高级）

class Student(object):
	pass

std = Student()
std.name="张三"
print(std.name)

#实例绑定一个方法
def set_age(self,age):
	self.age = age

from types import MethodType
std.set_age = MethodType(set_age,std)
std.set_age(25)
print(std.age)

#给一个实例绑定的方法，对另一个实例是不起作用的
#为了给所有实例都绑定方法，可以给class绑定方法
def set_socre(self,score):
	self.score = score

Student.set_socre = MethodType(set_socre,Student)

std.set_socre(99)
print(std.score)

std1 = Student()
std1.set_socre(88)
print(std1.score)

#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

class Student(object):
	__slots__ = ('name','age')

s = Student()
s.name = '李理理'
print(s.name)

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
	pass

g = GraduateStudent();
g.score = 110
print(g.score)
