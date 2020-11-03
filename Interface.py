import wx
from threading import Thread

from TerrariaFishingBot import TerraBot
from pynput import keyboard


def get_monitor_size():
    displays = (wx.Display(i) for i in range(wx.Display.GetCount()))
    sizes = [display.GetGeometry().GetSize() for display in displays]
    sizes = list(sizes[0])
    sizes = [int(size/5) for size in sizes]
    return sizes


def get_icon(icon_path):
    icon = wx.Icon()
    icon.CopyFromBitmap(wx.Bitmap(icon_path, wx.BITMAP_TYPE_ANY))
    return icon


class TerraInterface(wx.Frame):
    def __init__(self, parent, title):
        super(TerraInterface, self).__init__(parent, title=title, size=get_monitor_size())
        self.panel = wx.Panel(self)
        self.slider = wx.Slider(self.panel, value=50, minValue=1, maxValue=100,
                                style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        self.btn = wx.ToggleButton(self.panel, -1, "Turn On")
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetIcon(get_icon("icon.ico"))

        self.bot = TerraBot()

        self.initialise()
        self.initialise_listener()
        self.initialise_bot()

    def initialise(self):
        # Initialises buttons and sliders
        self.vbox.Add(self.slider, 1, flag=wx.EXPAND | wx.TOP, border=20)
        self.slider.Bind(wx.EVT_SLIDER, self.on_scroll)
        self.vbox.Add(self.btn, 0, wx.ALIGN_CENTER)
        self.btn.Bind(wx.EVT_TOGGLEBUTTON, self.change_state)
        self.panel.SetSizer(self.vbox)
        self.Centre()
        self.Show(True)

    def initialise_listener(self):
        listener = keyboard.Listener(
            on_release=self.on_release)
        listener.start()

    def initialise_bot(self):
        thread = Thread(target=self.bot.start_program)
        thread.daemon = True
        thread.start()

    def change_state(self, *args):
        self.bot.on = not self.bot.on
        self.btn.SetValue(self.bot.on)
        self.update_button(self.bot.on)

    def on_release(self, key):
        # Checks if "f" key was pressed, if it was, changes state of the program
        try:
            if key.char.lower() == "f":
                self.change_state()
        except AttributeError:
            pass

    def update_button(self, state):
        # Updates button label
        if state:
            self.btn.SetLabel("Turn Off")
        else:
            self.btn.SetLabel("Turn On")

    def on_scroll(self, event):
        # Adjusts the sound volume in the volume recorder when slider changes (Real time)
        value = event.GetEventObject().GetValue()
        self.bot.sound_recorder.volume = value


ex = wx.App()
TerraInterface(None, "TerraFishingBot")
ex.MainLoop()