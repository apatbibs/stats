#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 16:03:03 2026

@author: Home
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt


n = 10
mu = 0
sigma = 1




x = np.arange(1,10001)
Xbars = []
rangecount = 0
for k in range(10000):
    array = np.random.normal(mu, sigma, n)
    Xsum = 0
    for i in range(n):
        Xsum += array[i]
    Xbar = Xsum/n
    Xbars.append(float(Xbar))
    if Xbar > 1/m.sqrt(n):
        rangecount += 1
plt.scatter(x,Xbars,s=5)
plt.title("$\bar{X} Scatterplot")
plt.show()
plt.hist(Xbars, bins = 20, edgecolor='k', color='darkgray')
plt.title("The Average of $\bar{X}")
plt.savefig("HW2_3_2")

XbarFract = rangecount/10000
print(f"Fraction of X bar values above 1/sqrt(n) = {XbarFract}")
