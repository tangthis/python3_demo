#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis

#OOP面向对象编程

std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

print(print_score(std1))
print(print_score(std2))

class Student(object):
	"""docstring for Student"""
	def __init__(self, name,score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s:%s'% (self.name,self.score))

bart = Student('李唐',100)
lisa = Student('小明',87)
bart.print_score()
lisa.print_score()