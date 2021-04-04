consentToContinue = 'y'  # this is flag
#number1 = 0
#number2 = 0
#opSelector = 1


def inputs():
    global number1, number2, opSelector
    number1 = int(input('enter the first number:'))
    number2 = int(input('enter the second number:'))
    opSelector = int(input('select the operation to be performed :\n 1. add\t2. subtract\t3. multiply\t4. division'))
    return number1, number2, opSelector


def selector(z):
    if z == 1:
        print(add())
    elif z == 2:
        print(subtract())
    elif z == 3:
        print(multiply())
    elif z == 4:
        print(devide())
    else:
        print('please enter from the inputs listed below')
        z = int(input('select the operation to be performed :\n 1. add\t2. subtract\t3. multiply\t4. division'))


def add():
    return number1 + number2


def subtract():
    return number1 - number2


def multiply():
    return number1 * number2


def devide():
    return number1 / number2


while consentToContinue:
    if consentToContinue is 'y':
        inputs()
        selector(opSelector)
        consentToContinue = str(input('do you want more calculations?!. (y/n):\n'))
    elif consentToContinue is 'n':
        print('okay!! Bye!!')
        break
    else:
        print('please select the valid input')
        consentToContinue = str(input('do you want more calculations?!. (y/n):\n'))
