from pynput.mouse import Button, Controller
import time
mouse = Controller()

while True:
    mouse.press(Button.left)
    time.sleep(0.15)
    mouse.release(Button.left)
