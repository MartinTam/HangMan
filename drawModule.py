def hangingMan(error):
    
    if error == 1:
        print('_____')
    elif error == 2:
        hangingMan(error-1)
        print('     |')
    elif error == 3:
        hangingMan(error-1)
        print('    _', end="")
        
    elif error == 4:
        hangingMan(error-1)
        print('O', end="")
        
    elif error == 5:
        hangingMan(error-1)
        print('_')
        
    elif error == 6:
        hangingMan(error-1)
        print('     |')
    elif error == 7:
        hangingMan(error-1)
        print('    /', end="")
    elif error == 8:
        hangingMan(error-1)
        print(' \\')


def gameOver():
    print()
    print('-------------------------------------------')
    print('Game Over!')
    print()


def success():
    print('-------------------------------------------')
    print('Success!')
    print()