#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-20 23:47:41
# @Author  : xiaomi (ukyomud@outlook.com))
# @Filename : parameter.py
# @Description : practice parameters

def story(**kwds):
    return 'Once upon a time. There was a ' '%(job)s called %(name)s.' % kwds


def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)


def interval(start, stop=None, step=1):
    'Imitates range()) for step>0'
    if stop is None:
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i +=step
    return result

print(story(job='king',name='Gumby'))
# print(story(name='Jerry',job='king'))
# params = {'job':'language','name':'Python'}
# print(story(**params))
# del params['job']
# print(story(job='stroke of genius',**params))
print(power(2,3))
# print(power(3,2))
# print(power(y=3,x=2))
# params =(5,))*2
# print(power(*params))
# print(power(2,3,'Hello,World!'))
print(interval(10))
# print(interval(1,5))
# print(interval(3,12,4))
# print(power(*interval(3,7))))
