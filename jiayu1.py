#!/bin/env python3
#-*- coding:gbk -*-

'''
def numinput1():
    global a
    a = int(input('请输入一个整数:'))
count=0
while True:
    numinput1()
    count+=1
    if a == 5:
        print('Input %d You Win !' % (a))
        break
    if count >=3 :
        print('Input %d Times,You Lose !' % (count))
        break        

'''


def numinput1():
    global a
    a = int(input('请输入一个整数:'))

while True:
    a -=1
    print('*')
        
