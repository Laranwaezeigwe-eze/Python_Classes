import numpy as np

number = np.arange(1, 6)
print(number)
numbers = number.copy()
print(numbers)
# to show that numbers has a separate copy of number:
number *= 20
print(number)
print(numbers)
print('************************************')
# Method flatten deep copies the original copy
grades = np.array([[87,96,70],[100,87,90]])
print(grades)
flattened = grades.flatten()
print(flattened)
print(grades)
