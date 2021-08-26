nest_list= [[1, 2, 3], [4, 5, 6]]
for row in nest_list:
    for element in row:
       print(element, end=' ')
    print()

for i, row in enumerate(nest_list):
    for j, element in enumerate(row):
        print(f'a[{i}][{j}]= {element}', end=' ')
    print()

for i, row in enumerate(nest_list):
    print(f'row{i}')
    for j, element in enumerate(row):
        print(f'col{j} = {element}')
print(f'row {i} column{j}')

