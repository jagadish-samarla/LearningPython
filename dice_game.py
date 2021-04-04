import random
kannu = 1
chemma = 6

start = input('do you want to play the game? :\n (y/n) \n')

while start:
    if start is 'y':
        #print('game is starting now')
        print('and the value are .....')
        dice1 = random.randint(kannu, chemma)
        print(dice1)
        dice2 = random.randint(kannu, chemma)
        print(dice2)
        start = input(' do you want to play inputs: \n (y/n) \n')
    elif start is 'n':
        print('okay !! ending the game')
        break
    else:
        start = input('enter valid input \n (y/n) \n')
