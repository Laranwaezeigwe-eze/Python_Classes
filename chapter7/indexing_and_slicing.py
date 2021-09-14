import numpy as np

num = np.arange(1, 16).reshape(3, 5)
print(num)

print("using index and slice, select row 2:")
row_2 = num[2]
print(row_2)
print("select column 5:")
col_5 = num[:, 4]
print(col_5)
print("select row 0 and 1:")
row_0_1 = num[[0, 1]]
print(row_0_1)
print("column 2 to 4:")
col2_4 = num[:, 2:4]
print(col2_4)
print("element in row 1 and column 4:")
element = num[1, 3]
print(element)
print("all element from rows 1 & 2 that are in columns 0, 2 & 4:")
value = num[2,[0,2,4]]
# print(value)
