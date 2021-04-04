number = int(input('enter any number: '))

def factorial(n):
    if n == 1: # The termination condition
        return 1 # The base case
    else:
        res = n * factorial(n-1) # The recursive call
    return res
print('the factorial of given number is: ',factorial(number))

