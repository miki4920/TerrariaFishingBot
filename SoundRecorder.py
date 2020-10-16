import soundcard as sc
import time
CHUNK = 1024


def get_default_device():
    default_speaker = sc.default_speaker().name
    default_speaker_microphone = sc.get_microphone(default_speaker, include_loopback=True)
    return default_speaker_microphone


class SoundRecorder(object):
    def __init__(self, volume=50):
        # Initialises recorder, gets an index of Stereo Mix Device
        self.device = get_default_device()
        self.volume = volume

    def check_volume(self):
        # Second sound variable required to ignore fishing rod sounds
        second_sound = False
        while True:
            with self.device.recorder(samplerate=48000) as stream:
                data = stream.record(numframes=CHUNK)
                for sound_point in data:
                    sound_point = sum(sound_point)-1
                    if sound_point > self.volume/100:
                        if not second_sound:
                            second_sound = True
                            time.sleep(1.5)
                            break
                        else:
                            return True
