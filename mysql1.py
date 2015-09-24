#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis
# mysql数据库操作

import mysql.connector
conn = mysql.connector.connect(host='192.168.2.182',port=33066,user='root', password='123456', database='test')
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ['1'])
values = cursor.fetchall()
print(values)