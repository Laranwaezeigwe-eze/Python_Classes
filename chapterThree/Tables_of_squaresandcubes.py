number = 0
print(f'{"number"} {"square":>10} {"cube":>10}')
for number in range(6):

    square = int(number ** 2)
    cube = int(number ** 3)
    print(f'{number:>5} {square:>10} {cube:>10}')

