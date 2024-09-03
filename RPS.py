#Written by Anthony A
#2 September 2024
import random

while True:
    a = int(input('Type 1 to play classic Rock, Paper, Scissors. Type 2 to play Rock, Paper, Scissors, Lizard, Spock. '))
    #Error occurs if '' is inputted
    if a == 1 or a == 2:
        break
    else:
        print('Please answer with 1 or 2. ')

if a == 1:
    print('===================')
    print('Rock Paper Scissors')
    print('===================')

    print('1) ✊')
    print('2) ✋')
    print('3) ✌️')

    player = int(input('Pick a number: '))
    computer = random.randint(1,3)

    if player == 1:
        print('You chose: ✊')
    elif player == 2:
        print('You chose: ✋')
    elif player == 3:
        print('You chose: ✌️')

    if computer == 1:
        print('CPU chose: ✊')
    elif computer == 2:
        print('CPU chose: ✋')
    elif computer == 3:
        print('CPU chose: ✌️')


    if player == computer:
        print('It\'s a draw!')
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print('The Player won!')
    else:
        print('The CPU won!')
        

    


elif a == 2:
    print('================================')
    print('Rock Paper Scissors Lizard Spock')
    print('================================')

    print('1) ✊')
    print('2) ✋')
    print('3) ✌️')
    print('4) 🦎')
    print('5) 🖖')

    player = int(input('Pick a number: '))
    computer = random.randint(1,5)

    if player == 1:
        print('You chose: ✊')
    elif player == 2:
        print('You chose: ✋')
    elif player == 3:
        print('You chose: ✌️')
    elif player == 4:
        print('You chose: 🦎')
    elif player == 5:
        print('You chose: 🖖')

    if computer == 1:
        print('CPU chose: ✊')
    elif computer == 2:
        print('CPU chose: ✋')
    elif computer == 3:
        print('CPU chose: ✌️')
    elif computer == 4:
        print('CPU chose: 🦎')
    elif computer == 5:
        print('CPU chose: 🖖')

    if player == computer:
        print('It\'s a draw!')
    elif (player == 1 and computer == 3) or (player == 1 and computer == 4):
        print('The Player won!')
    elif (player == 2 and computer == 1) or (player == 2 and computer == 5):
        print('The Player won!')
    elif (player == 3 and computer == 2) or (player == 3 and computer == 4):
        print('The Player won!')
    elif (player == 4 and computer == 5) or (player == 4 and computer == 2):
        print('The Player won!')
    elif (player == 5 and computer == 1) or (player == 5 and computer == 3):
        print('The Player won!')
    else:
        print('The CPU won!')
    