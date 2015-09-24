#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# for x in xx 表示循环
names=['张胜男','李强','Machial','李章','Tom']
for name in names:
	print(name)

#0-100的整数序列
r = range(101)
lr = list(r)
sum = 0
for ll in lr:
	sum += ll
print(sum)

#while
n = 200
sum1 = 0
while n > 100:
	sum1 += n
	n = n-1
print(sum1)


