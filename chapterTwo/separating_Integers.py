user = int(input("Enter 5 digit integer: "))
print(user)
first_digit = (user // 10000)
second_digit = (user % 10000 // 1000)
third_digit = (user % 1000 // 100)
fourth_digit = (user % 100 // 10)
fifth_digit = (user % 10)

print(first_digit, "   ", second_digit, "   ", third_digit, "   ", fourth_digit, "   ", fifth_digit)
