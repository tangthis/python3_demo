#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#list
classmates=['张三','李四','王五']
print(classmates)
print('classmates len:%d' % len(classmates))

#往list中追加元素到末尾
classmates.append('赵六')
print(classmates)

#往list中插入元素
classmates.insert(1,'大拿')
print(classmates)

#删除list末尾的元素
classmates.pop();
print(classmates)
classmates.pop(1)
print(classmates)


#list里面的元素的数据类型也可以不同
L=['a',1,True]
print(L)
LS=['list中套list',L,1]
print(LS)

#有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates1 = ('Michale','Tom','Lee')
print(classmates1)

#注意：tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！