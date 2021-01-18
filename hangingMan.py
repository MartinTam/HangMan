import subprocess
import drawModule

subprocess.call("clear")

password = ['1', '2', '3', '4', '5']
enter = ['_', '_', '_', '_', '_']
error = 0
find = False
done = 0


while enter != password:
    print()
    print()
    print('Type the password:', enter[0], enter[1], enter[2], enter[3], enter[4])
    word = input()
    subprocess.call('clear')


    for i in range(len(password)):
        if word == password[i] and enter[i] != password[i]:
            enter[i] = password[i]
            
            find = True
            
            if enter == password:
                drawModule.hangingMan(error)
                print()
                print()
                print('Type the password:', enter[0], enter[1], enter[2], enter[3], enter[4])
                print()
                drawModule.success()
                done = 1
    
    if done == 1:
        break

    if find == False:
        error += 1
    else:
        find = False
    
    if error != 0:
        drawModule.hangingMan(error)

        if error == 8:
            print()
            print('Type the password:', enter[0], enter[1], enter[2], enter[3], enter[4])
            drawModule.gameOver()
            break
    