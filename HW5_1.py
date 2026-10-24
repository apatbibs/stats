#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:14:49 2026

@author: Home
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 1. 

n = 20
beta0 = 1
beta1 = 1
sigma = 0.1

x = np.arange(n)/n
eps = np.random.normal(0, sigma, n)

y = beta0 + beta1*x + eps

plt.scatter(x,y,s=2)
plt.title('Sample Plot of n = 20')
plt.minorticks_on()
plt.grid(which='major',linestyle='-',alpha=0.8)  
plt.grid(which='minor',linestyle='--',alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig("HW5_1.png")
plt.show()



# 2. 

def compute(x, y):
    ybar = np.mean(y)
    xbar = np.mean(x)
    
    b1 = np.sum((x-xbar)*(y - ybar))/(np.sum((x - xbar)**2))
    b0 = ybar - b1*xbar
    return b0, b1

b0_manl, b1_manl = compute(x,y)
print(b0_manl, b1_manl)


# 3.

b1_comp, b0_comp, r_val, p_val, std_err = stats.linregress(x, y)
print(b0_comp, b1_comp)

# 4.
#95% CI
#b1 and beta hat are interchangable (p. 492), the book uses beta hat so I'm shifting to that for this problem, 
#though I'm starting with my already computed b0 and b1 variables from #2

alpha = 0.05

df = n-2
SSE = np.sum((y - b0_comp + b1_comp*x)**2)

s = np.sqrt(SSE/df)

S_xx = np.sum((x - np.mean(x)) ** 2)
s_beta1 = s/np.sqrt(S_xx)


t_crit = stats.t.ppf(1 - alpha/2, df)

ci_lower = b1_comp - t_crit*s_beta1
ci_upper = b1_comp + t_crit*s_beta1
print(f'CI interval = [{ci_lower} < b_1 < {ci_upper}')