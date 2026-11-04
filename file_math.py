#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:03:06 2026

@author: alli
"""

import numpy as np

arr = np.arange(10)
print(arr)

# save usuli orqali saqlash

arr = np.save('data', arr)
# saqlangan malumotni qayta chop qilish

arr2 = np.load('data.npy')
print(arr2)



# savez usuli
# 1 ta faylda bir nechta arraylar sqlaydi

arr = np.arange(10)
arr1 = np.arange(20)


np.savez('arrays', a = arr, b = arr1)

arrays = np.load('arrays.npz')

print(arrays['a'])
print(arrays['b'])


# savez_compressed usuli

arr = np.arange(10)
arr1 = np.arange(20)


np.savez_compressed('array_compressed', a = arr, b = arr1)

array = np.load('array_compressed.npz')

print(array['a'])
print(array['b'])
 



# savetxt usulu
# 2 o'lchamli massiv

data  = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
    ])

# saqlash
np.savetxt('data.csv', data, delimiter=',', fmt='%d')

# qayta yuklash

data2 = np.loadtxt('data.csv', delimiter=',', dtype=int)

print(data2)
















