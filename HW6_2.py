#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:46:22 2026

@author: Home
"""
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

x = [55.10, 44.83, 46.32, 51.10, 49.89, 45.20, 48.18, 46.70, 54.31, 41.50, 47.50, 52.00, 52.25, 50.86, 51.66, 54.77, 57.06, 57.84, 55.22]
y = [49.10, 31.20, 32.80, 42.60, 42.50, 32.70, 36.21, 40.40, 37.42, 30.80, 35.34, 44.80, 41.75, 39.35, 44.07, 43.40, 45.30, 39.08, 41.89]

n = len(x)

S_xx = np.sum((x-np.mean(x))**2)
S_yy = np.sum((y-np.mean(y))**2)
S_xy = np.sum((x-np.mean(x))*(y-np.mean(y)))

r = S_xy/(np.sqrt(S_xx)*np.sqrt(S_yy))

v = n-2
 
z = 0.5*np.log((1+r)/(1-r))*np.sqrt(n-3)

P = 2*(1 - stats.norm.cdf(abs(z)))

print(f'r = {r}')
print(f'P = {P}')

plt.scatter(x, y,s=7.5)
plt.title('y vs x')
plt.minorticks_on()
plt.grid(which='major',linestyle='-',alpha=0.8)
plt.grid(which='minor',linestyle='--',alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("HW6_2.png")
plt.show()