

import random

word_bank = ['skech', 'nala', 'bentley', 'lily', 'melo', 'coffee', 'cream', 'luna']

word = random.choice(word_bank)

a = input('Please type easy, medium, or hard to choose difficulty. ')

if a == 'easy':
    attempts = 12
elif a == 'medium':
    attempts = 7
elif a == 'hard':
    attempts = 4
else:
    print('Bruh. Choose a difficulty.')

print('Welcome to the word guessing game! You will have ' + str(attempts) + ' tries to guess the word.')

guessed_word = ['_'] * len(word)

while attempts > 0:
    print('\nCurrent word:' + ' '.join(guessed_word))
    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print('Great guess!')
    else: 
        attempts -= 1
        print('Wrong guess! You have ' + str(attempts) + ' attempts left.')

    if '_' not in guessed_word:
        print('You have correctly guessed the word! The word was ' + word + '.')
        break
else:
    print('You did not guess the word. The word was ' + word + '.')
