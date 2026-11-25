#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:28:09 2026

@author: Home
"""
import numpy as np
n = 10
theta_hat = 4/10 #p_hat = theta_hat

z_alphadiv2 = 2.576
q_hat = 1 - theta_hat
p_tilde = (theta_hat + z_alphadiv2**2/(2*n))/(1 + z_alphadiv2**2/(n))
CI_pos = p_tilde + z_alphadiv2 * np.sqrt((theta_hat*q_hat/n) + (z_alphadiv2**2)/(4*n**2))/(1+z_alphadiv2**2/n)
CI_neg = p_tilde - z_alphadiv2 * np.sqrt((theta_hat*q_hat/n) + (z_alphadiv2**2)/(4*n**2))/(1+z_alphadiv2**2/n)
delta = z_alphadiv2 * np.sqrt((theta_hat*q_hat/n) + (z_alphadiv2**2)/(4*n**2))/(1+z_alphadiv2**2/n)
# What does .2 mean here?
print(f"CI range for theta_hat = .2: {CI_neg, CI_pos}")

Large_CI_pos = p_tilde + z_alphadiv2 * np.sqrt(theta_hat*q_hat/n)
Large_CI_neg = p_tilde - z_alphadiv2 * np.sqrt(theta_hat*q_hat/n)

print(f"CI Large range for theta_hat = .2: {Large_CI_neg, Large_CI_pos}")