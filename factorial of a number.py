number = int(input('enter the number to find the factorial: \n'))
iterationResult = number

if number is 0:
    print('factorial of "0" or "1" is = 1 .')
else:
    for i in range(1, number):
        iterationResult *= i

    print('the factorial of {} is {} '.format(number, iterationResult))
