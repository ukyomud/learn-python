#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-20 23:43:30
# @Author  : xiaomi (ukyomud@outlook.com)
# @Filename : fibonacci.py
# @Description : The Fibonacci sequence

def fibs(number):

    result = [0, 1]

    for i in range(number):
        result.append(result[-2] + result[-1])

    return result

print(fibs(10))
