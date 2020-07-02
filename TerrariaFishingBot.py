from pynput import keyboard
from pynput.mouse import Controller, Button
import time
import sounddevice as sd
import numpy as np


class TerraBot(object):
    def __init__(self):
        self.on = False
        self.mouse = Controller()
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
        print(indata if indata[0] > 0.1 and indata[1] > 0.1 else 0)
        volume_norm = np.linalg.norm(indata) * 10

    def fishing_loop(self):
        self.mouse.press(Button.left)
        duration = 150
        with sd.Stream(channels=1, callback=self.callback):
            sd.sleep(int(duration * 1000))


TerraBot()


f

"""Set sound mixer to default device, make sounddevice use the default device, figure out keyboard handling, which does not interfere with the loop."""