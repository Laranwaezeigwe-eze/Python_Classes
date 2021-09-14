counter = 0
sum_total = 0
average = 0
product = 1
while counter < 4:
    user_input1 = int(input("Enter number: "))
    counter = counter + 1
    sum_total = sum_total + user_input1
print("Total of the sum is: ", sum_total)
average = sum_total / 4
print("Average is: ", average)
while counter < 4:
    user_input1 = int(input("Enter number: "))
    product = product * user_input1
    counter = counter + 1
print("Product is: ", product)
largest = 0
smallest = 0
temp = 0
while counter < 4:
    user_input = int(input("Enter number: "))
    if largest > user_input:
        largest = user_input
    counter = counter + 1
print("Largest number is: ", largest)

