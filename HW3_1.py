#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:04:03 2026

@author: Home
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy.stats import binom

np.random.seed(42)


sample = np.random.normal(0,1,10)
print(np.mean(sample))

p = 900/(1000*24)
n = 24








hr = np.random.binomial(n=1, p=p, size = 24*1000)

day = hr.reshape(1000, 24).sum(axis=1)
xmax = 2  
x = np.arange(0, xmax + 1)
P_P = []

# ------------------------1a--------------------------

simulated_counts = np.bincount(day, minlength = xmax+1)[:xmax+1]
P_S = simulated_counts / 1000


# ------------------------1b--------------------------

#lam = p/dt
#P_x (P_P for 1a) = ((p/dt)*t)**x*np.exp((-p/dt)*t)
for n in x:
    P_x = ((p*n)**n*m.exp((-p*n)))/m.factorial(n)
    P_P.append(P_x)

# ------------------------1c--------------------------
P_B = binom.pmf(x,n = 24,p = p)


plt.plot(x, P_S, label='$P_S(x)$', color='k')
plt.plot(x, P_P, label='$P_P(x)$', color='r')
plt.plot(x, P_B, label='$P_B(x)$', color='b')
plt.xlabel('Number of Flares per Day ($x$)')
plt.ylabel('Probability of Occuring')
plt.title('Probability vs Counts')
plt.minorticks_on()
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()


# --- QUESTION 2: Time Between Flares ---
# Find indices where a flare occurred (in hours)
flare_hours = np.where(hr == 1)[0]

# Calculate time intervals between successive flares
time_between_flares = np.diff(flare_hours)

# Plotting Question 2
plt.figure(figsize=(10, 5))
plt.hist(time_between_flares, bins=30, edgecolor='k', color='g', density=True)
plt.xlabel('Time Between Flares (Hours)')
plt.ylabel('Density')
plt.title('Histogram of Time Intervals Between Successive Flares')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
