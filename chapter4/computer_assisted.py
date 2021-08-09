import random


def learn_multiplication():
    for _ in range(3):
        number = random.randrange(10)
        number2 = random.randrange(7)
        answer = number * number2
        question = int(input(f'How much is {number} times {number2} ?'))
        if question == answer:
            print("Very good!")
            # print(question)
        if question != answer:
            print("No. Please try again")


learn_multiplication()
