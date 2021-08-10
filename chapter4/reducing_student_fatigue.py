import random


def multiplication():
    for _ in range(3):
        response = ['Very good', 'Nice work', 'Keep up the good work!']
        response2 = ['No.Please try again.', 'Wrong.Try once more', 'No.Keep trying.']
        response = random.choice(response)
        response2 = random.choice(response2)
        number = random.randrange(10)
        number2 = random.randrange(7)
        answer = number * number2
        question = int(input(f'How much is {number} times {number2} ?'))
        if question == answer:
            print(response)
        if question != answer:
            print(response2)


multiplication()
