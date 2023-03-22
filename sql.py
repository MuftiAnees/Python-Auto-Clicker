import subprocess
import pyautogui
from time import sleep

subprocess.Popen(
    'C:\Program Files\MySQL\MySQL Workbench 8.0 CE\MySQLWorkbench.exe')
sleep(30)
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.click(240, 525)
sleep(25)
pyautogui.click(293, 147)
sleep(5)
pyautogui.click(1917, 3)
