
"""A module for recording, transcribing, and summarizing audio files using various APIs and models.

Classes:
    Recorder: a class for recording audio files
    Summarizer: a class for summarizing text using a specified model and configuration
    Transcriber: a class for transcribing audio files using various APIs

Functions:
    main(config_file: str = 'config.yml', debug: bool = False): the main function for recording, transcribing, and summarizing audio files. Uses the Recorder, Transcriber, and Summarizer classes.
"""
import os

import fire
import openai
import whisper

from recorder import Recorder
from summarizer import Summarizer
from transcriber import Transcriber

openai.api_key = os.getenv("OPENAI_API")

model = whisper.load_model("base")

recorder = Recorder()
transcriber = Transcriber()


def main(
    config_file="config.yml",
    debug=False
):
    try:
        while True:
            filename = recorder.record()

            if debug:
                recorder.playback(filename)

            s2text = transcriber.transcribe(filename)
            print(s2text)

            summarizer = Summarizer.from_config(config_file)
            print(summarizer.summarize(s2text))

            print()
            print("#" * 80)
            input("press any key to try again, ctrl-D to exit")
            print("#" * 80)
            print()
    except KeyboardInterrupt:
        print("exiting...")


if __name__ == '__main__':
    fire.Fire(main)
