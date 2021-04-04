import random
numberInput = int(input('enter the number to be guess between (1-100):\n'))
numberToBeGuessed = random.randint(1, 100)
numberOfTrails = 0
while numberInput:
    numberOfTrails +=1
    if numberOfTrails == 6:
        print('Sorry!! you have exceeded max limits of trails')
        print('the actual number is :\n ', numberToBeGuessed)
        break
    else:
        if numberInput < numberToBeGuessed:
            print('your number is less\n you have completed {} out of 6 trails'.format(numberOfTrails))
            if 1 <= numberOfTrails <= 2:
                print("don't worry you have plenty of trails!!")
            elif 2 < numberOfTrails <= 4:
                print("time to take a wild guess")
            elif numberOfTrails >4:
                print("you almost nearby. One proper guess could win the game ")
            numberInput = int(input('guess another number between (0-100):\n '))
        elif numberInput > numberToBeGuessed:
            print('your guess is greater \n you have completed {} out of 6 trails'.format(numberOfTrails))
            if numberInput < numberToBeGuessed:
                print('your number is less\n you have completed {} out of 6 trails'.format(numberOfTrails))
                if 1 <= numberOfTrails <= 2:
                    print("don't worry you have plenty of trails!!")
                elif 2 < numberOfTrails <= 4:
                    print("time to take a wild guess")
                elif numberOfTrails > 4:
                    print("you almost nearby. One proper guess could win the game ")

            numberInput = int(input('guess another number between (0-100):\n '))
        elif numberInput == numberToBeGuessed:
            print('your guess is right. you have taken {} out of 6 moves to complete'.format(numberOfTrails))
            break
