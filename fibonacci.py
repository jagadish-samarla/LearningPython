user_input = int(input('enter how many fibonacci numbers to be printed (not less than 3): \n'))
fibonacci = [1, 1]


def append_fibonacci(n):
    """this function appends the next fibonacci element into the list """
    next_number = fibonacci[n-1]+fibonacci[n-2]
    fibonacci.append(next_number)


for i in range(2, user_input):
    append_fibonacci(len(fibonacci))

print(fibonacci)