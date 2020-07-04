import pyaudio
import audioop

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10


class SoundRecorder(object):
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.dev_index = self.get_dev_index()

    def get_dev_index(self):
        for i in range(self.p.get_device_count()):
            dev = self.p.get_device_info_by_index(i)
            if dev['name'] == 'Stereo Mix (Realtek(R) Audio)' and dev['hostApi'] == 0:
                return dev['index']

    def check_volume(self, volume):
        stream = self.p.open(format=FORMAT,
                             channels=CHANNELS,
                             rate=RATE,
                             input=True,
                             input_device_index=self.dev_index,
                             frames_per_buffer=CHUNK)
        second_sound = False
        for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
            data = stream.read(CHUNK)
            rms = audioop.rms(data, 2)

            if rms > volume:
                if not second_sound:
                    second_sound = True
                else:
                    break
        stream.stop_stream()
        stream.close()
        return True
