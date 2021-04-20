import random
compare = None
recent_guess = random.randint(0, 100)
count = 0
print('Please keep some Random number (0-100) in your mind, and let me guess it. \n Here we go')


def print_random(x, y, z):
    """this function will display the guess and gets the feedback from the user"""
    x = +1
    #y = random.randint(0, 100)
    print('My guess is : \t', y)
    z = int(input('let me know how accurate i guess: '
          '1. matched \t 2. higher \t 3. lower'))
    return x, z


print_random(count, recent_guess, compare)
while compare:
    if compare == 1:
        print('i won in ', count, 'moves')
        break
    elif compare == 2:
        recent_guess = random.randint(0, recent_guess)
        print_random(count, recent_guess, compare)
    elif compare == 3:
        recent_guess = random.randint(recent_guess, 100)
        print_random(count, recent_guess, compare)
