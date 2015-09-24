#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis

#实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
#变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    def set_score(self, score):
    	if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('黎明',98)
print(bart.print_score())