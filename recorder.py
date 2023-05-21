import os
import queue
import sys
import tempfile
import threading

import numpy as np
import sounddevice as sd
import soundfile as sf

assert np


class Recorder:
    """
    This class is used to record and playback audio.
    """
    def __init__(self):
        self.input_device_id, self.output_device_id = sd.default.device

        input_device_info = sd.query_devices(self.input_device_id, 'input')
        self.input_fs = int(input_device_info['default_samplerate'])
        self.input_channels = input_device_info['max_input_channels']

        output_device_info = sd.query_devices(self.output_device_id, 'output')
        self.output_fs = int(output_device_info['default_samplerate'])
        self.output_channels = output_device_info['max_output_channels']

    def record(self, verbose: bool = False) -> str:
        dirname = tempfile.mkdtemp()
        tmpfile = os.path.join(dirname, "recording.wav")

        buffer = queue.Queue()
        def callback(indata, frames, time, status):
            """This is called (from a separate thread) for each audio block."""
            if status:
                print(status, file=sys.stderr)
            buffer.put(indata.copy())

        try:
            with sf.SoundFile(tmpfile, mode='x', samplerate=self.input_fs, channels=self.input_channels) as f:
                with sd.InputStream(
                    samplerate=self.input_fs,
                    channels=self.input_channels,
                    device=self.input_device_id,
                    callback=callback
                ):
                    print('#' * 80)
                    print('press Ctrl+C to stop the recording')
                    print('#' * 80)
                    while True:
                        f.write(buffer.get())
        except KeyboardInterrupt:
            if verbose:
                print(f"Recorded to {tmpfile}")

        return tmpfile

    def playback(self, filename: str, verbose: bool = False):
        event = threading.Event()

        data, fs = sf.read(filename, always_2d=True)
        current_frame = [0]

        def callback(outdata, frames, time, status):
            if status:
                print(status)
            chunksize = min(len(data) - current_frame[0], frames)
            outdata[:chunksize] = data[current_frame[0]:current_frame[0] + chunksize]
            if chunksize < frames:
                outdata[chunksize:] = 0
                raise sd.CallbackStop()
            current_frame[0] += chunksize

        try:
            stream = sd.OutputStream(
                samplerate=fs, device=self.output_device_id, channels=self.output_channels,
                callback=callback, finished_callback=event.set)

            if verbose:
                print('press Ctrl+C to stop the playback')
                print('#' * 80)

            with stream:
                event.wait()  # Wait until playback is finished
        except KeyboardInterrupt:
            print("Stopping early...")


if __name__ == "__main__":
    r = Recorder()
    filename = r.record()
    r.playback(filename)
