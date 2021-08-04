passes = 0
failures = 0

total_count = 0
while total_count < 10:
    result = int(input('Enter result (1=pass, 2=fail): '))
    if result == 1:
        passes = passes + 1
    if result == 2:
        failures = failures + 1
    total_count = passes + failures
print("Passed: ", passes)
print("Failed: ", failures)
print(total_count)

