from pynput import keyboard
from pynput.mouse import Controller, Button
import time


class TerraBot(object):
    def __init__(self):
        self.on = False
        self.mouse = Controller()
        listener = keyboard.Listener(
            on_release=self.on_release)
        listener.start()
        self.start_program()

    def on_release(self, key):
        try:
            if key.char == "f":
                self.on = not self.on
        except AttributeError:
            pass

    def start_program(self):
        while True:
            while self.on:
                self.fishing_loop()
                break

    def fishing_loop(self):
        self.mouse.press(Button.left)
        time.sleep(0.01)
        self.mouse.release(Button.left)
        time.sleep(2)







terraBot = TerraBot()