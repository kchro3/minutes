"""This module is for recording, transcribing, and summarizing audio files.

This module is intended to be run from the command line.

Example:
    $ python file.py

    # press any key to record, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D to exit

    # press any key to try again, ctrl-D
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
