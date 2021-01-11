import pyautogui
import time
import keyboard
import random
import win32api, win32con
import mouse

# takes screen shot of certain region
im1 = pyautogui.screenshot(region=(534,430,828,231,))
im1.save("screenshot.png")


#mouse cursor
pyautogui.displayMousePosition()

#click pywin32 function
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)



#checks image on screen
while 1:
    if pyautogui.locateOnScreen('ball.png', confidence=0.9) != None:
        print("i see")
        image = pyautogui.locateOnScreen('ball.png', confidence=0.8)
        
        if image != None:
            x, y = pyautogui.center(image)
            pyautogui.moveTo(x,y)
            time.sleep(0.1)
    else:
        print("i cant see")
        time.sleep(0.5)
