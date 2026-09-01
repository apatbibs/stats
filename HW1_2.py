#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 13:49:51 2026

@author: Home
"""

#1. 3^3 = 27 step configurations

#2.

import numpy as np
import random
import matplotlib.pyplot as plt

a = [-1, 1]

# Experiment: Randomly select an element from the list a

result = random.choice(a)
end = 4000
# Repeat the experiment n times

finalcount1 = 0

for n in range (1,end+1):
    results = []
    
    for exp in range(0, 3):
    
      result = random.choice(a)
    
      results.append(result)
    print(results)
    if sum(results) == 1:
        finalcount1 = finalcount1+1
print(f"Nuber of times final count = 1: {finalcount1}")
print(f"Nuber of trials: {end}")

prob = finalcount1/end
print(f"Probability that the final position is 1: {prob}%")
