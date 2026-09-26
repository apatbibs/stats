#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 18:42:58 2026

@author: Home
"""
import numpy as np
import matplotlib.pyplot as plt


n = 10
mu = 0
sigma = 1




x = np.arange(1,10001)
S2_bs = []
rangecount = 0
for k in range(10000):
    array = np.random.normal(mu, sigma, n)
    Xsum = 0
    Ssum = 0
    for i in range(n):
        Xsum += array[i]
    Xbar = Xsum/n
    for j in range(n):
        Ssum += (array[j]-Xbar)**2
    S2_b = Ssum/n
    S2_bs.append(float(S2_b))

plt.scatter(x,S2_bs,s=5)
plt.title("$S_b^2$ Scatterplot")
plt.show()
plt.hist(S2_bs, bins = 20, edgecolor='k', color='darkgray')
plt.title(f"The Average of $S_b^2$ = {np.mean(S2_bs):.2f}")
plt.savefig("HW3_3_2.png")
