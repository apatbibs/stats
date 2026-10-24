#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:07:46 2026

@author: Home
"""
#1. 
# y = [0, -1, 0, 1]
#a0 = ybar = (0+1+0-1)/4 = 0

#a_i = 2/N * "Summation from t = 0 to N-1":(y_t)*cos(2pi*i/N*t)
#a_1 = 2/4[(0)*cos(2pi*(1/4)*0) + (-1)*cos(2pi*(1/4)*1) + (0)*cos(2pi*(1/4)*2) + (1)*cos(2pi*(1/4)*3)]
#a_1 = 2/4[0+0+0+0] = 0
#a_2 = 2/4[(0)*cos(2pi*(2/4)*0) + (-1)*cos(2pi*(2/4)*1) + (0)*cos(2pi*(2/4)*2) + (1)*cos(2pi*(2/4)*3)]
#a_2 = 2/4[0+0+0+0] = 2/4[0+1+0-1] = 0

#b_i = 2/N * "Summation from t = 0 to N-1":(y_t)*sin(2pi*i/N*t)
#b_1 = 2/4[(0)*sin(2pi*(1/4)*0) + (-1)*sin(2pi*(1/4)*1) + (0)*sin(2pi*(1/4)*2) + (1)*sin(2pi*(1/4)*3)]
#b_1 = 2/4[0-1+0-1] = -2/2 = -1
#b_2 = 2/4[(0)*sin(2pi*(2/4)*0) + (-1)*sin(2pi*(2/4)*1) + (0)*sin(2pi*(2/4)*2) + (1)*sin(2pi*(2/4)*3)]
#b_2 = 2/4[0+0+0+0] = 0


#2. 
import numpy as np
import sympy as sp

def dft(y):
    N = len(y) #N = 4
    if N % 2 == 0:
        q = N//2 
    else:
        q = (N - 1)//2
    a = np.zeros(q)
    b = np.zeros(q)
    a0 = np.mean(y)
    
    for i in range(1,q+1):
        f_i = i/N
        for t in range(0,N):      
            a[i-1] += (2/N)*(y[t]*sp.cos(2*sp.pi*f_i*t))
            b[i-1] += (2/N)*(y[t]*sp.sin(2*sp.pi*f_i*t))            
    return a0, a, b

# Test case
a0, a, b = dft(np.array([0, -1, 0, 1]))
print(a0) # 0.0
print(a)  # [0.0  0.0]
print(b)  # [-1.0 0.0]