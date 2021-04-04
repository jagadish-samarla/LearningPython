number = int(input('enter any number to find whether prime or not: '))

def is_prime(n):
    if n < 2:
        return 'prime number starts with 2'
        #return True
    else:
        for i in range(2, n):
            n % i == 0
            #return 'it is not a prime number'
            return False

        else:
            #return 'it is a prime number'
            return True

print(is_prime(number))