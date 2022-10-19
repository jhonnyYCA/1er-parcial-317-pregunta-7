# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:20:45 2022

@author: fx_66
"""


n = 2000000



pi=1
imp=1
for i in range(1,n):
    imp=1/((i*2)+1)
    if(i%2==0):
        pi += imp
    else:
        pi -= imp
spi=0  
for i in range(4):
    spi+=pi

print ("pi= ",spi)