def calculate_product(*args):
    product = 1
    for value in args:
        product = product * value
    return product


print(calculate_product(2, 3,5,6))
