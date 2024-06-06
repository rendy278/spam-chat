import time
import pyautogui

time.sleep(4)
spamchat = open('spam.txt')

for line in spamchat:
    pyautogui.typewrite(line)
    pyautogui.press('enter')