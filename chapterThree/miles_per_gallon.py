counter = 0
total = 0
total2 = 0

user_input = 0.0
user_input2 = 0.0
user_input = float(input("Enter gallon used (-1 used to stop): "))
while user_input != -1:
    # user_input = float(input("Enter gallon used (-1 used to stop): "))
    user_input2 = float(input("Enter miles driven: "))
    total = total + user_input
    total2 = total2 + user_input2
    user_input = float(input("Enter gallon used (-1 used to stop): "))
milesPerGallon = user_input2 / user_input
print("The miles/ gallon for this tank is: ", milesPerGallon)

average = total2 / total
print("The overall average miles/gallon is: ", average)
