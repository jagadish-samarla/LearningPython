import random

consent = True
#uc = None  # uc means user choice
three_options = ["Rock", "Paper", "Scissor"]


def consent_to_start():
    """ a function that asks the user to start the game or not """
    x = str(input('Do you want to play rock paper scissors again?! ( y / n) \n:'))
    return x


def user_choice():
    """a function that asks the user to choose rock paper or scissor"""
    global uc
    uc = str(input('choose anything from Rock(r), paper(p) or scissor(s) !?? (r/p/s) \n'))
    return uc


def compare(x):
    """a function to compare both choices"""
    y = random.choices(three_options)
    if x == y:
        print(" That's a tie, we both chosen the same")
        #consent_to_start(consent)
    else:
        if (x == 'r' and y == 'scissor') or (x == 'p' and y == 'rock') or (x == 's' and y == 'paper'):
            print('Yayy!!, You won , i chosen', y)
        elif (x == 'r' and y == 'paper') or (x == 'p' and y == 'scissor') or (x == 's' and y == 'rock'):
            print('You lost!!, i chosen', y)
        #consent_to_start(consent)


while consent:
        user_choice()
        compare(user_choice())
        consent_to_start()
        if consent == 'y':
            continue
        elif consent == 'n':
            print('Okay! Bye Bye!')
            break
        else:
            print('enter valid key \n')
            consent_to_start()

