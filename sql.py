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

# # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
# pyautogui.move(None, 10)
# pyautogui.doubleClick()  # Double click the mouse at the
# # Use tweening/easing function to move mouse over 2 seconds.
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
# # Type with quarter-second pause in between each key.
# pyautogui.write('SET GLOBAL sql_mode ="";')
# pyautogui.write('SET SESSION sql_mode ="";', interval=0.25)
# pyautogui.press('esc')  # Simulate pressing the Escape key.
# pyautogui.keyDown('shift')
# pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
# pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'c')
