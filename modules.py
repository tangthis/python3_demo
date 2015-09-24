#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis

# 模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释 
' a test module '

__author__ = 'Michael' #使用__author__变量把作者写进去


import sys
def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello world!')
	elif len(args) == 2:
		print('Hello %s!' % args[1])
	else:
		print('Too many args !')

#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__ == '__main__':
	test()


#作用域

#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用

def _priviate_1(name):
	print('Hello,%s' % name)

def _private_2(name):
	return 'Hi,%s' % name

def greeting(name):
	if len(name) > 3:
		return _priviate_1(name)
	else:
		return _private_2(name)