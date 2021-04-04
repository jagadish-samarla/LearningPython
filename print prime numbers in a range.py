upperNumber = int(input('enter upper range number: \n'))
lowerRange = int(input('enter lower range number: \n'))

#set = []
if upperNumber <= 2:
    print('prime numbers starts with 2!!!')

else:
    for i in range(lowerRange, upperNumber + 1):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            print(i, ' ')