#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 07:48:01 2026

@author: alli
"""

import numpy as np


# names = (['Sarvar','Abdullo', 'Hasan', 'Abdullo', 'Hasan'])
# ints = ([4,4,4,3,3,3,1,1,1,2,2,2,6,6,])

# #unique ro'yxatdagi takrorlanmas elemetlarni qaytaradi
# #(takrorlansa ham faqat bittasini qabul qiladi) set kabi

# print(np.unique(names))
# print(np.unique(ints))

#intersect1d usuli
#data


# arr1 = ([2,2,3,3,1,1,5,5,6])
# arr2 = ([1,2,3,4,5,6,7,8])

# #arr2 dagi elementlarni arr1 mavjudligini tekshirish
# print(np.intersect1d(arr1, arr2))


#setdiff1d va union1d usuli

names1 = np.array(['Hasan', 'Husan', 'Olim','Ali','Vali','Abdullo','Iqbal'])
names2 = np.array(['Olim','Ali','Vali','Abdullo','Iqbal'])
# np.setdiff1d() Birinchi massivda bor, ikkinchisida yo‘q elementlar
# union1d() Ikkala massivdagi barcha noyob elementlar
print(np.setdiff1d(names1, names2))
print(np.union1d(names1, names2))
