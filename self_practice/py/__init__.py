# is_old = False
#
# is_licensed = False
#
# if is_old:
#     print("You are old enought to drive!")
# elif is_licensed:
#     print("You can drive now!")
# else:
#     print("You are not old enough!")

# is_magician = True
# is_expert = True
#
# if is_magician and is_expert:
#     print("You are a master magician")
# if is_magician and not is_expert:
#     print("at least you're getting there")
# if not is_magician:
#     print("You need magic powers")

# for item in [1,2,3,4]:
#     for next_item in ['tin','can','milk','juice']:
#         print(item, next_item)

# counter = 0
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in my_list:
#     counter = counter + number
# print(counter   )
#
# import random
# frequency1 =0
# frequency2 =0
# frequency3 = 0
# frequency4 = 0
# frequency5 = 0
# frequency6 = 0
# for roll in range(6000000):
#     face = random.randrange(1,7)
#     if face == 1:
#         frequency1 += 1
#     elif face == 2:
#         frequency2 += 1
#     elif face == 3:
#         frequency3 +=1
#     elif face == 4:
#         frequency4 += 1
#     elif face == 5:
#         frequency5 += 1
#     elif face == 6:
#         frequency6 += 1
# print(f'Face{"Frequency":>10}')
# print(f'{1:>2}{frequency1:>10}')
# print(f'{2:>2}{frequency2:>10}')
# print(f'{3:>2}{frequency3:>10}')
# print(f'{4:>2}{frequency4:>10}')
# print(f'{5:>2}{frequency5:>10}')
# print(f'{6:>2}{frequency6:>10}')


# for char in enumerate("Hello sir"):
#     print(char)
#
# for i, char in enumerate((1,2,3)):
#     print(i,char)
# Enumerate is useful if u need the index of the item you are looping through.

# for i, char in enumerate(list(range(100))):
#      if(char == 60):
#          print(f'index of 60: {i}')

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# x=7
# print(id(x))
#
# values=[1,2,3]
# print(sum(values))
# print(values)
#
# import statistics
# population = 1,3,4,2,6,5,3,4,5,2
# print(statistics.pvariance(population))
# sd=statistics.pstdev(population)
# print(sd)
# varyin=statistics.variance(population)
# print(varyin)
# print(statistics.stdev(population))
# x=[1,2,3,4,5]
# def mystery(x):
#     y = 0
#     for value in x:
#         y +=value **2
#         print(y)
#     return  y
# print("Mystery: ",mystery(x))
#
# price = [10,20,30]
# total = 0
# for cost in price:
#     total= cost+total
# print(total)

# def factorial(n):
#     if n==0:
#         return 1
#     if n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(900))

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# for i in range(5):
#     print(fibonacci(i))

# _cache={}
# def fibonacci(n):
#     if n== 0:
#         return 0
#     elif n == 1:
#         return 1
#     if n in _cache:
#       return _cache[n]
#     else:
#         result = fibonacci(n-1) + fibonacci(n-2)
#         _cache[n] = result
#         return  result
#
# for i in range(900):
#     print(fibonacci(i))

# import time
#
# _cache = {}
#
#
# def factorial(n):
#     if n == 1:
#         return 1
#     if n == 0:
#         return 1
#     if n in _cache:
#         return _cache[n]
#     else:
#         result = n * factorial(n - 1)
#         _cache[n] = result
#         time.sleep(1)
#         return result
#
#
# for i in range(21, 1, -1):
#     # time.sleep(1)
#     print(factorial(i))

# character = []
# character +='Birthday'
# print(character)

# student_tuple = ('Amanda','Bintu',[2,45,6])
# first_name, second_name, grades = student_tuple
# print(first_name, second_name, grades)
# print()
# first, second ='Be'
# print(f'{first} {second}')
# print()
# number1, number2, number3 = range(10, 40, 10)
# print(f'{number1} {number2} {number3}')

# SWAPPING VALUES VIA PACKING AND UNPACKING
# number1 = 20
# number2 = 40
# number3 = 10
# number4 = 5
# number1, number2, number3, number4 = (number3, number4, number2, number1)
# print(f'number1 ={number1}; number2 ={number2}; number3 = {number3}; number4 ={number4}')

# # ACCESSING INDICES AND VALUES VIA BUILT-IN FUNCTION ENUMERATE
# colors = ['red', 'orange', 'blue']
# print(list(enumerate(colors)))
# print(tuple(enumerate(colors)))
# print()

# DISPLAYING A BAR CHART
# number = [20, 5, 7, 17, 3]
# print(f'Index{"Value":>10}     Bar')
# for index, value in enumerate(number):
#     print(f'{index:>5} {value:>8}    {"*" * value}')
# print()
# print()
#
# high_low = ('Monday', 280, 62)
# print(high_low)
# print(f'{high_low[0]}: High={high_low[1]}, Low={high_low[2]}')
# day, high, night = high_low
# print(f'high_low={day}; high_low={high}; high_low{night}')
#
# print()

# numbers = list(range(1, 16))
# print(numbers)
# print(numbers[1:16:2])
# numbers[5:10]=[0,0,0,0,0]
# print(numbers)
# print(numbers[:5])
# numbers[:]=[]
# print(numbers)
# numbers = list(range(1,16))
# print(numbers)
# del numbers[:4]
# print(numbers)
# del numbers[::2]
# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 94, 1, 9]
# numbers.sort(reverse=True)
# print(numbers)
#
# food = ['Cookies', 'pizza', 'Grapes', 'apple', 'steak', 'Bacon']
# food.sort()
# print(food)
# veggie = ['carrot', 'brocoli', 'Grapes', 'spinach']
# food.extend(veggie)
# print(food)
#
# print()
#
# responses = [1, 2, 3, 4, 5, 3, 4, 2, 4, 2, 3, 1, 4]
# for i in range(1, 6):
#     print(f'{i} appears {responses.count(i)} times')
# print()
#
# rainbow = ['green', 'orange', 'violet']
# print(rainbow)
# print(f'the index of violet is: {rainbow.index("violet")}')
# rainbow.insert(2, 'red')
# print(f'To insert: {rainbow}')
# rainbow.append('yellow')
# print(f'to append: {rainbow}')
# rainbow.reverse()
# print(f'reverse method: {rainbow}')
# rainbow.remove('orange')
# print(f'To remove orange element from list: {rainbow}')

# STACK APPEND/PUSH AND POP- PRINCIPLE OF LIFO
stack=[]
stack.append('red')
stack.append("blue")
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

# LIST COMPREHENSION
# colors= ['red','blue','orange','lilac','purple','lemon']
# color=[item.upper() for item in colors]
# print(colors)
# print(color)

# cubes= [(number, number ** 3) for number in range(1,6)]
# print(cubes)
# multiples =[number for number in range(3, 30, 3)]
# print(multiples)
# print()
# number =[10,3,7,1,9,4,2]
# cube= list(x **3 for x in number if x%2==0)
# print(cube)

# FILTERING WITH THE BUILT IN FILTER FUNCTION
number = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]


def is_odd(x):
    return x % 2 != 0


print(list(filter(is_odd, number)))
# LAMBDA EXPRESSION OF THE ABOVE FUNCTION
# lambda parameter_list: expression
print(list(filter(lambda x: x % 2 != 0, number)))

# USING A BUILT-IN FUNCTION MAP AND LAMBDA TO SQUARE EACH VALUE IN NUMBERS:
print(list(map(lambda x: x ** 2, number)))

# COMBINING THE FILTER, MAP AND LAMBDA OPERATION TOGETHER:
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, number))))

numbers = list(range(1, 16))


def is_even(y):
    return y % 2 == 0


print(list(filter(lambda y: y % 2 == 0, numbers)))
print(list(map(lambda y: y ** 2, numbers)))
print(list(map(lambda y: y ** 2, filter(lambda y: y % 2 == 0, numbers))))

fahrenheit = [41, 32, 212]
celsius = list(map(lambda x: (x, (x - 32) * 5 / 9), fahrenheit))
print(celsius)
print(ord('o'))
print()
height = [69, 77, 54]
var = [(x, x * 0.0254) for x in height]
print(var)
print(list(map(lambda x: (x, x * 0.0254), height)))

