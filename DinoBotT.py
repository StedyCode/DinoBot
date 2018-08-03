import pyautogui
import time

def restart():
    pyautogui.keyDown('down')
    pyautogui.click(482, 294)



def jump():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print("Jump!")
    time.sleep(0.05)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

restart()
jump()
play = True
while play:
    try:

        start = time.clock()

        if start <= 60:

            plant = pyautogui.pixel(305, 326)

            if plant != (247,247,247):

                jump()


        if start >= 30:

            plant = pyautogui.pixel(330, 326)


        if start >=60:
            plant = pyautogui.pixel(0,0)



    except Exception as e:
        play = False
        print(e)

