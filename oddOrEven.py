num = int(input('enter any number here: \n'))

if num % 2 == 0:
    if num % 4 == 0:
        print("Wow!! that's a leap year")
    else:
        print('you have picked an even number')
else:
    print('You have picked an odd number')