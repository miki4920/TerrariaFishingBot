from SoundRecorder import SoundRecorder
from pynput.mouse import Controller, Button
import time


class TerraBot(object):
    def __init__(self):
        self.on = False
        self.sound_recorder = SoundRecorder()
        self.mouse = Controller()

    def start_program(self):
        # Continuous loop which only executes fishing part when program is on
        while True:
            while self.on:
                self.fishing_loop()

    def click(self):
        # A function responsible for clicking, 0.05 delay so the game can detect click
        self.mouse.press(Button.left)
        time.sleep(0.05)
        self.mouse.release(Button.left)

    def fishing_loop(self):
        # Throws the float, listens for volume, catches fish and then waits two seconds to repeat again (Reeling
        # takes approximately 2 seconds)
        self.click()
        if self.sound_recorder.check_volume():
            self.click()
        time.sleep(2)
