import random

computer_number = random.randint(1000, 9999)
count = 0
user_guess = 0
number = None


def ask_to_guess():
    global count, user_guess
    count += 1
    user_guess = int(input('Guess the four digit number : \n'))
    return user_guess


def split_numbers(x):
    global number
    digits = []
    while x > 0:
        digits.append(x % 10)
        x = int((x - x % 10) / 10)
    digits = digits[::-1]
    return digits


def compare(x, y):
    cows = 0
    bulls = 0
    #while x != y:
    for i in range(0, 4):
        for j in range(0, 4):
            if x[i] == y[j]:
                if i == j:
                    cows += 1
                elif i != j:
                    bulls += 1
        print(cows, ' cows')
        print(bulls, ' bulls')
        ask_to_guess()


ask_to_guess()
y = split_numbers(computer_number)
while user_guess != computer_number:
    x = split_numbers(user_guess)
    compare(x, y)
else:
    print('You won the game in {} moves'.format(count), 'and the correct number is :', computer_number)