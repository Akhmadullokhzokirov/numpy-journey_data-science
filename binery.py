#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 04:41:55 2026

@author: alli
"""


import numpy as np

# arr = np.random.randn(6)
# arr2 = np.random.randn(6)

# # print(arr)
# # print(arr2)

# # arr3 = np.add(arr,arr2)
# # print(arr3)

# # arr3 = np.multiply(arr,arr2)
# # print(arr3)

# arr3 = np.maximum(arr,arr2)
# print(arr3)


# xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
# yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])

# #shart

# cound = np.array([True,False, True, True, False])

# result = np.where(cound, xarr, yarr)
# print(result)



arr = np.random.randn(4,4)
print(arr)


results = np.where(arr < 0, -7.5, 3)
print(results)