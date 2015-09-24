#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis
# 枚举

from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan)


#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum,unique

@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1


print(Weekday.Sun)
print(Weekday.Sun.value)
		