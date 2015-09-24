#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

print('包含中文字符str')

#获取字符整数表示
ord('A')
ord('中')

#chr()把编码转成对应字符
chr(66)
chr(25991)

#如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#bytes类型的数据用带b前缀的单引号或双引号表示
x = b'ABC'

#以Unicode表示的str通过encode()方法可以编码为指定的bytes
'ABC'.encode('ascii')
'中文'.encode('utf-8')

#要计算str包含多少个字符，可以用len()函数：
len('中文')
len('ABC')

#格式化输出
print('Hi,%s,you have $%d' % ('Michale',100000))