"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""
from pynput.mouse import Controller, Button
import pyaudio
import wave
import audioop
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 30
WAVE_OUTPUT_FILENAME = "output.wav"
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if dev['name'] == 'Stereo Mix (Realtek(R) Audio)' and dev['hostApi'] == 0:
        dev_index = dev['index'];
        print('dev_index', dev_index)


stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                input_device_index = dev_index,
                frames_per_buffer = CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    rms = audioop.rms(data, 2)
    if rms > 7000:
        mouse = Controller()
        mouse.press(Button.left)
        time.sleep(0.01)
        mouse.release(Button.left)
    if rms > 0:
        print(rms)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

