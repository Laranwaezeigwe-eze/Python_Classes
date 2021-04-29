number1 = int(input("Enter first integer: "))
number2 = int(input("Enter second integer: "))
number3 = int(input("Enter third integer:  "))

sum = (number1 + number2 +number3)
print("Sum is:",sum)

average = sum /3
print("Average is:", average)

product = (number1 * number2 * number3)
print("Product is:", product)

smallest = number1
if number2 < smallest:
    smallest = number2
if number3 < smallest:
    smallest = number3
print("Smallest number:",smallest)

largest = number1
if number2 > largest:
    largest = number2
if number3 > largest:
    largest = number3
print("Largest number:",largest)
