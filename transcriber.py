import whisper


class Transcriber:
    def __init__(self, model: str = "base"):
        self.model = whisper.load_model(model)

    def transcribe(self, filename: str):
        result = self.model.transcribe(filename)
        s2text = result["text"]
        return s2text
