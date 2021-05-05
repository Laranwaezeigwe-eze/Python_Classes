

user_input = input("What is your problem?")
print(user_input)
user_input2 = str(input("Have you had this problem before(yes or no): ?"))
print(user_input2)
# for count in range(2):

if user_input2 =='yes':
    print('Well, you have it again.')
elif user_input2 == 'no':
    print('Well, you have it now.')
else:
    user_input = input("What is your problem?")
