#!/bin/env python3
#coding:gbk

import time
import random
import sys
import os
import subprocess
import platform

def checksystem():
    if 'Windows' in platform.system() :
        subprocess.call("cls", shell=True) # windows��ִ��cls����
    if 'Linux' in platform.system() :    
        subprocess.call("clear") # linux�Ͻ�����callִ��clear����  

checksystem() 
    
print('����ʷ��ķ')
hp = int(100) #���Ѫ��
hp2 = int(100) #ʷ��ķѪ��
hh = int(0)
print('��ĵ�ǰѪ��%d and ʷ��ķ��Ѫ��%d' % (hp,hp2))
print('ս����ʼ��')


#����ж�
def zdjieguo(x,y):
    if y <= 0 and x > 0:
        print('���Ѫ��:%d VS ʷ��ķ��Ѫ��:%d' %(x,y))
        print('��ɱ����ʷ��ķ��ȡ������ʤ����')        
        print('����������������������������������������')
        input('���س�������...')
        os._exit(0)
    if x <= 0 and y > 0:
        print('���Ѫ��:%d VS ʷ��ķ��Ѫ��:%d' %(x,y))
        print("�㱻ʷ��ķɱ��������ʧ�ܣ�")        
        print('����������������������������������������')
        input('���س�������...')
        os._exit(0)

def yourount(mhp,dhp2,mdm,ddm2,mbj):
    global hp2 
    if mbj > 30 :
        hp2 = dhp2-2*mdm
        print('���ʷ��ķ���𹥻� -%d ������' % (2*mdm))
        zdjieguo(mhp,hp2)

    if bj <= 30 :
        hp2 = dhp2 - mdm
        print('���ʷ��ķ���𹥻� -%d ��' % (mdm))
        zdjieguo(mhp,hp2)

def dmrount(mhp,dhp2,mdm,ddm2,dbj2):
    global hp
    if dbj2 > 30 :
        hp = mhp - 2*ddm2
        print('ʷ��ķ���㷢�𹥻� -%d ������' % (2*ddm2))
        zdjieguo(hp,dhp2)

    if dbj2 <= 30 :
        hp = mhp - ddm2
        print('ʷ��ķ���㷢�𹥻� -%d ��' % (ddm2))
        zdjieguo(hp,dhp2)

while (hp> 0 and hp2 >0):
    hh = hh + 1
    dm = random.randint(8,10) #��Ĺ�����
    dm2 = random.randint(6,11) #ʷ��ķ������
    bj = random.randint(0, 100) #��ı������ʼ���
    bj2 = random.randint(0, 70) #ʷ��ķ�ı������ʼ���
    speed = random.randint(0,20) #��������ٶ�
    speed2 = random.randint(0,10) #ʷ��ķ�������ٶ�
    print('�غ�%d:' % (hh))

    if speed >= speed2 :
        print('����������')
        yourount(hp,hp2,dm,dm2,bj)
        dmrount(hp,hp2,dm,dm2,bj2)
    if speed < speed2 :
        print('ʷ��ķ���������')
        dmrount(hp,hp2,dm,dm2,bj2)
        yourount(hp,hp2,dm,dm2,bj)
    if speed == 0 :
        print('�������ˣ�δ�ܹ�����')       
        dmrount(hp,hp2,dm,dm2,bj2)
    if speed2 == 0 :
        print('ʷ��ķ�����ˣ�δ�ܹ�����')       
        yourount(hp,hp2,dm,dm2,bj)
#ս����־
    print('���Ѫ��:%d VS ʷ��ķ��Ѫ��:%d' %(hp,hp2))
    print('����������������������������������������')
    #input('���س�������...')
    #checksystem() 