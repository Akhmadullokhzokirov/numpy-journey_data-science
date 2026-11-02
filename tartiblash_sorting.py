"""
NumPy: massivlarni tartiblash (sorting)

Mavzular:
    - np.sort() va arr.sort() farqi
    - o'sish va kamayish tartibida saralash
    - 2D massivda axis=0 va axis=1
"""

# %% Kutubxona
import numpy as np


# %% 1D massiv
arr = np.array([5, 2, 9, 1, 7])

# 1) np.sort(): yangi massiv qaytaradi
asc = np.sort(arr)
print(asc)  # [1 2 5 7 9]
print(arr)  # [5 2 9 1 7] o'zgarmadi

# 2) .sort(): asl massivni o'zgartiradi
arr_copy = arr.copy()
arr_copy.sort()
print(arr_copy)  # [1 2 5 7 9]

# 3) Kamayish tartibida
desc = np.sort(arr)[::-1]
print(desc)  # [9 7 5 2 1]


# %% 2D massiv
arr2d = np.array([[9, 4, 7, 1],
                  [3, 8, 2, 6],
                  [5, 1, 9, 0]])
print(arr2d.ndim)  # 2

# axis=0: har bir USTUN tartiblanadi
col_sorted = np.sort(arr2d, axis=0)
print(col_sorted)
# [[3 1 2 0]
#  [5 4 7 1]
#  [9 8 9 6]]

# axis=1: har bir QATOR tartiblanadi
row_sorted = np.sort(arr2d, axis=1)
print(row_sorted)
# [[1 4 7 9]
#  [2 3 6 8]
#  [0 1 5 9]]