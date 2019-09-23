from gpiozero import Button
from time import sleep
from signal import pause

switch = Button(18)
button = Button(4)
joyX = Button(22)
joyY = Button(23)

def switchState2():
    print("you are in switch state two")

def switchState1():
    print("you are in switch state one")
    if switch.is_pressed:
        switchState2()
    if button.is_pressed:
        print("button mode 1")


while True:
    if button.is_pressed:
        switchState1()
    if switch.is_pressed:
        print("switch on")
    if joyX.is_pressed:
        print("x")
    if joyY.is_pressed:
        print("y")
    sleep(1)

    button.when_released = switchState1
