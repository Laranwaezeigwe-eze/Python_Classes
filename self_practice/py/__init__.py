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

character = []
character +='Birthday'
print(character)

