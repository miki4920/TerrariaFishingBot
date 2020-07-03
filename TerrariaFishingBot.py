from pynput import keyboard
from SoundRecorder import SoundRecorder
from pynput.mouse import Controller, Button
import time


class TerraBot(object):
    def __init__(self):
        self.on = False
        self.mouse = Controller()
        self.sound_recorder = SoundRecorder()
        self.start_program()

    def click(self, button):
        self.mouse.press(button)
        time.sleep(0.05)
        self.mouse.release(button)

    def on_release(self, key):
        try:
            if key.char == "f":
                self.on = not self.on
        except AttributeError:
            pass

    def start_program(self):
        listener = keyboard.Listener(
            on_release=self.on_release)
        listener.start()
        while True:
            while self.on:
                self.fishing_loop()

    def fishing_loop(self):
        self.click(Button.left)
        if self.sound_recorder.check_volume():
            self.click(Button.left)
        time.sleep(2)


TerraBot()
