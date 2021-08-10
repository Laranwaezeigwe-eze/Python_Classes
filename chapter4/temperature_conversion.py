def fahrenheit():
    print(f'{"celsius":>10} {"fahrenheit":>10}')

    for C in range(0, 100):
        F = (9 / 5) * C + 32
        print(f'{C:>8}  {F:>8.2f}')
        C += 1


fahrenheit()
