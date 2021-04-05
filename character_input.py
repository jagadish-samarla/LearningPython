import datetime

name = input('Please enter your name: \n')
age = int(input('enter your age: \n'))
number = int(input('enter number of times message to be printed: \n'))
century = datetime.datetime.now().year - age + 100
for n in range(0, century):
    print('by {} you will become 100 years'.format(century))
