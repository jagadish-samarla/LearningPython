import random
actualNumber = random.randint(1, 10)
guessNumber = int(input('guess any number from (0-10) :\t'))
count = 0


#def inlets(x):
 #   x = int(input('guess any number: \t'))
  #  return x


#def increase(x):
 #   x = x+1
  #  return x

def compare(x, y):
    if x < y:
        return 'g'
    elif x > y:
        return 'l'
    elif x == y:
        return 's'


while guessNumber:
    count += 1
    if count < 3:
        compare(actualNumber, guessNumber)
        if compare(actualNumber, guessNumber) is 'g':
            print('your guess is greater')
            guessNumber = int(input(' guess another number: \t'))
        elif compare(actualNumber, guessNumber) is 'l':
            print('your guess is lower ')
            guessNumber = int(input('guess another number: \t'))
        elif compare(actualNumber, guessNumber) is 's':
            print('congratulations !! you have completed it in {} moves'.format((count)))
            break
    else:
        print('you have exceed maximum limits , and the number is \t', actualNumber)
        break


