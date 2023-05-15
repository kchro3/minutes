import os
import openai
import yaml


openai.api_key = os.getenv(\"OPENAI_API\")


class Summarizer:
    def __init__(self, model: str, temperature: int, max_tokens: int, prompt: str):
        self.model = model        self.temperature = temperature
        self.max_tokens = max_tokens
        self.prompt = prompt.strip()

    def summarize(self, text):
        prompt = self.prompt + ' ' + text

        response = openai.ChatCompletion.create(
            engine=self.model,
            prompt=prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            chat_history=[prompt],
            stop=None,
            n=None,
            presence_penalty=None,
            frequency_penalty=None,
            best_of=None,
            logprobs=None,
            echo=None,
            stop_sequence=None,
            user=None,
            model=None,
            temperature_sampling=None,
            max_new_tokens=None,
            max_tokens_length=None,
            no_repeat_ngram_size=None,
            num_samples=None,
            expand=None,
            **kwargs
        )

        return response.choices[0].text