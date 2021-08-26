word = 'The boy is rolling the stone and the stone got' \
       'rolling as the boy is rolling it'
word_count = {}

for new_word in word.casefold().split():
    if new_word in word_count:
        word_count[new_word] += 1
    else:
        word_count[new_word] = 1

for new_word, count in word_count.items():
    print(f'{new_word:<15}{count}')
