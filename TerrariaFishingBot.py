from SoundRecorder import SoundRecorder
from pynput.mouse import Controller, Button
import time


class TerraBot(object):
    def __init__(self):
        self.on = False
        self.sound_recorder = SoundRecorder()
        self.mouse = Controller()

    def click(self, button):
        self.mouse.press(button)
        time.sleep(0.05)
        self.mouse.release(button)

    def start_program(self):
        while True:
            while self.on:
                self.fishing_loop()

    def fishing_loop(self):
        print(1)
        self.click(Button.left)
        if self.sound_recorder.check_volume():
            self.click(Button.left)
        time.sleep(2)
