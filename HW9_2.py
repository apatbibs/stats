#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 20:09:40 2026

@author: Home
"""
import numpy as np
import math as m
from scipy.integrate import quad
import matplotlib.pyplot as plt


# 1. 
theta = 0.4
PDTheta = m.factorial(10)/(m.factorial(6)*m.factorial(4)) * theta**4*(1-theta)**6

 
print(f'1: {PDTheta}')
print()

# 2.


def f(x): return  m.factorial(10)/(m.factorial(6)*m.factorial(4)) * x**4*(1-x)**6
PD, err = quad(f, 0, 1)

# print(PD, err)

print(f'2: {PD}')
print()

# 3.

theta1 = np.linspace(0,1,100)
p = np.array((m.factorial(10)/(m.factorial(6)*m.factorial(4)) * theta1**4*(1-theta1)**6)/PD)

plt.scatter(theta1, p, s = 10)
plt.grid(which='major',linestyle='-',alpha=0.8)
plt.grid(which='minor',linestyle='--',alpha=0.5)
plt.xlabel(r'$\theta$')
plt.ylabel(r'p$(\theta|\mathcal{D})$')
plt.title(r'3: $\theta$ vs p($\theta$|$\mathcal{D})$', fontsize=13)
plt.savefig("HW9_2.png")



#4. 
# p(θ|𝒟) = P(𝒟|θ)p(θ)/P(𝒟)
# P(𝒟) = 10!/(6!*4!) * θ**4*(1-θ)**6
a = np.linspace(0.02, 0.1, 5)

print('4:')

def f2(x): return  (m.factorial(10)/(m.factorial(6)*m.factorial(4)) * x**4*(1-x)**6)/PD
for i in range(len(a)):
    aval = a[i]
    pthetaD, err = np.array(quad(f, 0, aval))
    print(f'for a = {aval}, p(θ|𝒟) = {pthetaD}')
# print(PD, err)

