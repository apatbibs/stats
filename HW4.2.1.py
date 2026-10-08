#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 16:11:12 2026

@author: Home
"""
import scipy
import numpy as np

s = np.sqrt(137324.3)
n = 17 #number of items in 1D array



chi2_1 = scipy.stats.chi2.ppf(0.025, n-1) 
chi2_2 = scipy.stats.chi2.ppf(0.975, n-1)  

print(f'Lower Chi^2: {chi2_1}')
print(f'Upper Chi^2: {chi2_2}')

CI_sig2_1 = ((n-1)*s**2)/chi2_1
CI_sig2_2 = ((n-1)*s**2)/chi2_2

print(f'CI for Sigma^2: ({CI_sig2_1}, {CI_sig2_2}')

CI_sig_1 = np.sqrt(CI_sig2_1)
CI_sig_2 = np.sqrt(CI_sig2_2)

# CIs are listed as [low, high]; you have backwards here.
# Also, follow instructions (file name and copy solution into comment)
print(f'CI for Sigma: ({CI_sig_1}, {CI_sig_2})')
