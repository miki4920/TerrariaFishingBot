from pynput import keyboard
from pynput.mouse import Controller, Button
import time
import sounddevice as sd
import numpy as np


class TerraBot(object):
    def __init__(self):
        self.on = False
        self.mouse = Controller()
        sd.default.device = 1
        self.start_program()

    def on_release(self, key):
        try:
            if key.char == "f":
                self.on = not self.on
        except AttributeError:
            pass

    duration = 5.5  # seconds

    def start_program(self):
        listener = keyboard.Listener(
            on_release=self.on_release)
        listener.start()
        while True:
            while self.on:
                self.fishing_loop()
                break

    def callback(self, indata, outdata, frames, time, status):
        volume_norm = np.linalg.norm(indata) * 10
        print("|" * int(volume_norm))
        time.sleep(0.01)
        self.mouse.release(Button.left)
        time.sleep(2)

    def fishing_loop(self):
        self.mouse.press(Button.left)
        duration = 15
        with sd.Stream(channels=2, callback=self.callback):
            sd.sleep(int(duration * 1000))



TerraBot()






