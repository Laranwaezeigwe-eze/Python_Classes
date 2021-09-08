import numpy as np

number = np.array([1, 4, 9, 16, 25, 36])
value = np.sqrt(number)

print(value)
print("********************************")

# add universal function
number2 = np.arange(1, 7) * 10
print(number2)
print("*************************")
add_func = np.add(number, number2)
print(add_func)
print("*************************")

# multiply universal function by scalar value 5
mult_func= np.multiply(number2, 5)
print(mult_func)
print("*************************")

# reshape number2 into a 2 by 3 array, then multiply value by a 1 dim:
num_reshape= number2.reshape(2, 3)
print(num_reshape)
number3 = np.array([2,4,6])
num3_multiply = np.multiply(number3,num_reshape)
print(num3_multiply)