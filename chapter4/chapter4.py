def maximum(value_1, value_2, value_3):
    max_value = value_1
    if value_2 > max_value:
        max_value = value_2
    if value_3 > max_value:
        max_value = value_3
    return max_value


value1 = (input("Enter first string: "))
value2 = (input("Enter second string: "))
value3 = (input("Enter third string: "))
print(maximum(value1, value2, value3))
