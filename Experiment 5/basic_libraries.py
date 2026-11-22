import math
import numpy as np
from scipy import stats

# -------------------------
# Math Library
# -------------------------
print("MATH LIBRARY")

number = 25

print("Square Root:", math.sqrt(number))
print("Power:", math.pow(2, 3))
print("Factorial:", math.factorial(5))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.3))

# -------------------------
# NumPy Library
# -------------------------
print("\nNUMPY LIBRARY")

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))

# Array operations
arr2 = np.array([1, 2, 3, 4, 5])

print("Addition of Arrays:", arr + arr2)
print("Multiplication of Arrays:", arr * arr2)

# -------------------------
# SciPy Library
# -------------------------
print("\nSCIPY LIBRARY")

data = [10, 20, 20, 30, 40, 50]

print("Mean:", stats.tmean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data, keepdims=True).mode[0])
print("Variance:", stats.tvar(data))
print("Standard Deviation:", stats.tstd(data))
