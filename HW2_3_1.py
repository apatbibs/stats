#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:20:35 2026

@author: Home
"""

import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.arange(1,10001)
Xbars = []
for k in range(10000):
    rng = np.random.default_rng()
    array = rng.normal(loc=0.0, scale=1.0, size=n)
    Xsum = 0
    for i in range(n-1):
        Xsum += array[i]
    Xbar = Xsum/n
    Xbars.append(float(Xbar))
    
plt.scatter(x,Xbars,s=5)
plt.title("$\bar{X} Scatterplot")
plt.show()
plt.hist(Xbars, bins = 20, edgecolor='k', color='darkgray')
plt.title("The Average of $\bar{X}")
plt.savefig("HW2_3_1")