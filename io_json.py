#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis
# IO

import os,json

f = open('D:/python/demo/basic.py','r',encoding='utf-8')
# r 只读
c = f.read()
print(c)

for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉


# w 写
# f.write()
# f.close()


print('os name %s' % os.name) #nt:windows

print('os enveronment %s' % os.environ)


#JSON
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
#{'age': 20, 'score': 88, 'name': 'Bob'}