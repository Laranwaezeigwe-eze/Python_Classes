import random

guess_number = random.randrange(1, 100)
for _ in range(10):
    guess = int(input("Guess my number between 1 and 100 with the fewest guesses: "))
    if guess > guess_number:
        print("Too High.")
        print(guess)
    elif guess < guess_number:
        print("Too Low")
        print(guess)
    else:
        print("Congratulations. You guessed the number!")
        break
