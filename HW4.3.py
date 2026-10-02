#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 21:23:01 2026

@author: Home
"""
#using simulation from 3_3_2

import numpy as np
import scipy

n = 10
mu = 0
sigma = 1
alpha = 0.05


x = np.arange(1,10001)
rangecount = 0
 
for k in range(10000):
    array = np.random.normal(mu, sigma, n)
    Xbar = np.mean(array)
    S = np.std(array, ddof=1)
    
    
    low_bound, up_bound = scipy.stats.t.interval(1 - alpha, df=n-1, loc=Xbar, scale=S/np.sqrt(n))
    
    if low_bound <= mu <= up_bound:
        rangecount += 1

Prob = rangecount/10000
# The empirical coverage probability should be very close to 1 - alpha (e.g., 0.95)
print(f'Probability: {Prob}')
print(f'Probability (1-alpha): {1-alpha}')
