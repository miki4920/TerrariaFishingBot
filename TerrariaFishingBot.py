
from SoundRecorder import SoundRecorder
from pynput.mouse import Controller, Button
import time


class TerraBot(object):
    def __init__(self, volume=18500):
        self.on = False
        self.volume = volume
        self.mouse = Controller()
        self.sound_recorder = SoundRecorder()

    def click(self, button):
        self.mouse.press(button)
        time.sleep(0.05)
        self.mouse.release(button)

    def start_program(self):
        while True:
            while self.on:
                self.fishing_loop()

    def fishing_loop(self):
        self.click(Button.left)
        if self.sound_recorder.check_volume(self.volume):
            self.click(Button.left)
        time.sleep(2)

