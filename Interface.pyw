import wx
from threading import Thread
from TerrariaFishingBot import TerraBot
from pynput import keyboard


def start_interface(name, *args):
    ex = wx.App()
    TerraInterface(None, name)
    ex.MainLoop()


class TerraInterface(wx.Frame):
    def __init__(self, parent, title):
        self.bot = TerraBot()
        self.on = False
        super(TerraInterface, self).__init__(parent, title=title, size=(250, 150))
        # Creates panel, button and slider
        self.panel = wx.Panel(self)
        self.sld = wx.Slider(self.panel, value=18500, minValue=10000, maxValue=25000,
                             style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        self.btn = wx.ToggleButton(self.panel, -1, "Turn On")
        # Adds an icon
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        # Initialises interface
        self.initialise()
        # Initialises I/O handler
        self.initialise_listener()
        self.initialise_bot()

    def initialise(self):
    # Initialises buttons and sliders
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.sld, 1, flag=wx.EXPAND | wx.TOP, border=20)
        self.sld.Bind(wx.EVT_SLIDER, self.on_scroll)
        vbox.Add(self.btn, 0, wx.ALIGN_CENTER)
        self.btn.Bind(wx.EVT_TOGGLEBUTTON, self.change_state)
        self.panel.SetSizer(vbox)
        self.Centre()
        self.Show(True)

    def initialise_listener(self):
        # Changes state of the program
        listener = keyboard.Listener(
            on_release=self.on_release)
        listener.start()

    def initialise_bot(self):
        # Starts bot in a separate thread
        thread = Thread(target=self.bot.start_program)
        thread.daemon = True
        thread.start()

    def change_state(self, e=None):
        # Changes state of the bot all across the program and updates the button
        self.on = not self.on
        self.bot.on = self.on
        self.btn.SetValue(self.on)
        self.update_button()

    def on_release(self, key):
        # Checks if "f" key was pressed, if it was, changes state of the program
        try:
            if key.char.lower() == "f":
                self.change_state()
        except AttributeError:
            pass

    def update_button(self):
    # Updates button label
        if self.on:
            self.btn.SetLabel("Turn Off")
        else:
            self.btn.SetLabel("Turn On")

    def on_scroll(self, e):
        # Adjusts the sound volume in the volume recorder when slider changes (Real time)
        value = e.GetEventObject().GetValue()
        self.bot.sound_recorder.volume = value


start_interface("TerraFishingBot")
