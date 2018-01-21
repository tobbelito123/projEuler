# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:55:33 2018

@author: Johan
"""
import time
t = 0
for i in range(100):
    t1 = time.time()
    l = [i for i in range(1000) if (i%3)==0 or (i%5) == 0]
    t += (time.time() - t1)

print(t/100)

print(sum(l))