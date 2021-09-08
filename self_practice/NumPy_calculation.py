import numpy as np
grades= np.random.randint(60,101,12).reshape(3,4)
print(grades)

average= grades.mean()
print('Average of all grades is: ',average)

average_col = grades.mean(axis=1)
print("Average of all grades in each column: ", average_col)

avg_row = grades.mean(axis=0)
print("Average of all grades in each row", avg_row)