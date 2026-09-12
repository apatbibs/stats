#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:17:55 2026

@author: Home
"""

import numpy as np
import matplotlib.pyplot as plt

n = 100
p = 0.4
q = 1-p
exp = 10000
x = np.linspace(0,10000,10000)

# You need to set n = 100 and the count the number of
# values with x=0, 1, 2, ..., n
P_x = np.random.binomial(n=n, p=p,size=exp)

print(P_x)

Px2 = (1/(np.sqrt(2*np.pi*n*p*q)))*np.exp(-(x-n*p)**2/(2*n*p*q))

plt.plot(x, P_x, color = 'k')
plt.plot(x, Px2, color = 'b', alpha = 0.5)

# Need to save before show because when you close the plot, there
# is nothing to save.
plt.savefig("HW2_4.png")
plt.show()
