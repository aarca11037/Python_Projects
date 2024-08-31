

import random

word_bank = ['Skech', 'Nala', 'Bentley', 'Lily', 'Melo', 'Coffee', 'Cream', 'Luna']

word = random.choice(word_bank)

a = input('Please type easy, medium, or hard to choose difficulty.')

if a == 'easy':
    attempts = 12
elif a == 'medium':
    attempts = 7
elif a == 'hard':
    attempts = 4
else:
    print('Bruh. Choose a difficulty.')



