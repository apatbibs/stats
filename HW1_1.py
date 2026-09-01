#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 20:33:07 2026

@author: Home
"""

#1. 
import numpy as np
import random
import matplotlib.pyplot as plt

a = [0, 1]

# Experiment: Randomly select an element from the list a

result = random.choice(a)

# Repeat the experiment n times
narray = np.arange(1,1001)

rf0s = []
rf1s = []

for n in range (1,1001):

    results = []
    
    for exp in range(1, n+1):
    
      result = random.choice(a)
    
      results.append(result)
    
    rf0 = results.count(0)/(n+1)
    rf1 = results.count(1)/(n+1)
    
    rf0s.append(rf0)
    rf1s.append(rf1)

    
    print(f"n = {n} experiments:")
    
    print(f"  Results: {results}")
    
    # rf = relative frequency
    
    print(f"  rf(0) = {results.count(0) / (n+1)}")
    
    print(f"  rf(1) = {results.count(1) / (n+1)}")
    
plt.plot(narray,rf0s,color='k',label="$rf(0)$") 
plt.plot(narray,rf1s,color='b',label="$rf(1)$") 
plt.title("rf(0) vs rf(1)")
ax = plt.gca()
ax.set_xlabel("n trials")
plt.legend()
plt.show()
plt.savefig("HW1_1.png")

#2.
# n = 3: 8 possible outcomes