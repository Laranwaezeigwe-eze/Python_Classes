p = 10000
n = 12
r = 8 / 100

time = int(input("What is the number of years amount will be compounded for? "))
print(time)
time_value = n * int(time)
print("The time value is: ",time_value)
rate = r/n
print("The nominal rate in years is: ", rate)

amount = p * (1 + rate)** time_value
print("Final amount after t years: ",amount)

