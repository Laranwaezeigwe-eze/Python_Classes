import numpy as np

number1 = np.arange(2, 19, 2).reshape(3, 3)
print("array", number1)
print()
number2 = np.arange(9, 0, -1).reshape(3, 3)
print("array", number2)
print()
combine_numbers = np.multiply(number1, number2)
print("array", combine_numbers)
