#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis

def is_odd(n):
	return n % 2 == 1

filter1 = filter(is_odd,[1,2,3,4,5,6,7,8,9,10])
print(list(filter1))

def not_empty(s):
	return s and s.strip()

filter2 = filter(not_empty,['A','','B','C','D','','','X','1'])
print(list(filter2))