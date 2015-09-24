#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis

class Student(object):
    pass

bart = Student()
print(bart)

bart.name='张三'
print(bart.name)

class Student(object):
	"""docstring for Student"""
	def __init__(self, name,score):
		super(Student, self).__init__()
		self.name=name
		self.score=score

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'


bart = Student('李王',88)
print(bart.name)
print(bart.get_grade())
		