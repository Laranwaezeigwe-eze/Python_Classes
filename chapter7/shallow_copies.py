import numpy as np

# create an array and a view of the array:

number = np.arange(1, 6)
print(number)
new_number = number.view()
print(new_number)
# using the built-in id function to see the difference
print(id(number))
print(id(new_number))

number *= 10
print(number)
print(new_number)