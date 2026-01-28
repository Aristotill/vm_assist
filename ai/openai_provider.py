"""
openai_provider.py
BYO-AI provider using environment variables.

No API keys are stored in code or repo.
"""

import os
from ai.provider import AIProvider

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


class OpenAIProvider(AIProvider):
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")

        if not self.api_key:
            raise RuntimeError(
                "OPENAI_API_KEY not set. Export it before using --ai."
            )

        if OpenAI is None:
            raise RuntimeError(
                "openai package not installed. Run: pip install openai"
            )

        self.client = OpenAI(api_key=self.api_key)

    def ask(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a cybersecurity assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()

