a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user_input = int(input('enter any number to bifurcate the list: \n'))
x = [numbers for numbers in a if numbers < user_input]
print(x)


