import os
import openai
import yaml


openai.api_key = os.getenv("OPENAI_API")


class Summarizer:
    def __init__(self, model: str, temperature: int, max_tokens: int, prompt: str):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.prompt = prompt.strip()

    def summarize(self, text):
        prompt = self.prompt + ' ' + text

        response = openai.Completion.create(
            model=self.model,
            prompt=prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )

        return response["choices"][0].text

    @classmethod
    def from_config(cls, config_file: str):
        with open(config_file, "r") as f:
            config = yaml.safe_load(f)["chatgpt"]

        return Summarizer(
            model=config["model"],
            temperature=config["temperature"],
            max_tokens=config["max_tokens"],
            prompt=config["prompt"]
        )
