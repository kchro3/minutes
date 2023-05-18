import os
"""This script records audio, transcribes it, and summarizes the text.

The script uses the Recorder, Transcriber, and Summarizer classes to perform these tasks. The Recorder class records audio, the Transcriber class transcribes the audio to text, and the Summarizer class summarizes the text.

The script uses the openai and whisper libraries to perform these tasks. The openai library is used to access the OpenAI API, and the whisper library is used to load the summarization model.

The script can be run from the command line using the Fire library. The script takes two optional arguments: config_file and debug. The config_file argument specifies the path to the configuration file, and the debug argument specifies whether to play back the recorded audio.

Args:
    config_file (str): Path to the configuration file.
    debug (bool): Whether to play back the recorded audio.

"""
The script uses the Recorder, Transcriber, and Summarizer classes to perform these tasks. The Recorder class records audio, the Transcriber class transcribes the audio to text, and the Summarizer class summarizes the text.

The script uses the openai and whisper libraries to perform these tasks. The openai library is used to access the OpenAI API, and the whisper library is used to load the summarization model.

The script can be run from the command line using the Fire library. The script takes two optional arguments: config_file and debug. The config_file argument specifies the path to the configuration file, and the debug argument specifies whether to play back the recorded audio.

"""import openai
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
