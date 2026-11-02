#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 06:24:26 2026

@author: alli
"""

import numpy as np

# A = np.arange(9).reshape(3, 3)
# print(A)

arr = np.array(10)
# np.sqrt(arr)
# print(arr)

# np.square(arr)
# print(arr)

# np.exp(arr)
# print(arr)

# np.log(arr[1:])
# print(arr) ishlamadi

arr1 = np.random.randn(6)
# # print(arr1)

# qoldiq,butun = np.modf(arr1)
# # print(qoldiq)
# # print(butun)

# np.sign(arr1)
# print(arr1) 

# np.isnan(arr1)
# print(arr1)

arr1[0] = np.nan
print(arr1)

np.isnan(arr1)
print(arr1)







