def duplicate():
    word = 'To be or not to be is a matter of choice and the choice you make all depends on you'
    unique_words = set(word.casefold().split(" "))
    for word in sorted(unique_words):
        print(word, end=" ")


duplicate()
