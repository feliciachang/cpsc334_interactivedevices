from gpiozero import Button
from time import sleep
from signal import pause

switch = Button(18)
button = Button(4)
joyX = Button(22)
joyY = Button(23)
mode = 0

def switchState3():
    while mode is 3:
        print("you are in switch state three")
        button.when_released = modeCounter
        if switch.is_pressed:
            print("switch says apple")
        elif joyX.is_pressed:
            print("joy x says bottle")
        elif joyY.is_pressed:
            print("joy y says cat")
        sleep(1)

def switchState2():
    while mode is 2:
        print("you are in switch state two")
        button.when_released = modeCounter
        if switch.is_pressed:
            print("switch says a")
        elif joyX.is_pressed:
            print("joy x says b")
        elif joyY.is_pressed:
            print("joy y says c")
        sleep(1)

def switchState1():
    while mode is 1:
        print("you are in switch state one")
        button.when_released = modeCounter
        if switch.is_pressed:
            print("switch says 1")
        elif joyX.is_pressed:
            print("joy x says 2")
        elif joyY.is_pressed:
            print("joy y says 3")
        sleep(1)

def modeOperator():
    global mode
    if mode == 0:
        print(mode)
        mode += 1
        switchState1()
    elif mode == 1:
        mode += 1
        switchState2()
    elif mode == 2:
        mode = 0
        switchState3()

def modeCounter():
    global mode
    button.when_released = modeOperator

while  True:
    modeCounter()
    sleep(1)
