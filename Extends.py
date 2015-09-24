#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis
# 继承和多态

class Animal(object):
	"""docstring for Animal"""
	def run(self):
		print('Animal is running')

class Dog(Animal):
	def run(self):
		print('Dog is running...')

	def eat(self):
		print('Dog eating meat...')

class Cat(Animal):
	pass


dog = Dog()
dog.run()

cat = Cat()
cat.run()

dog.eat()
		