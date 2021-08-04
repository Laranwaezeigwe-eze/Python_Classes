principal = 10000
rate = 0.07
for year in range(1, 31):
    amount = principal * (1 + rate) ** year
    print(f'{year:>2} {amount:>8.2f}')
