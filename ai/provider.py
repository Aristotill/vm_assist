
"""
provider.py
BYO-AI provider interface.

AI is untrusted. This module ONLY returns text.
"""

class AIProvider:
    def ask(self, prompt: str) -> str:
        raise NotImplementedError


class DummyProvider(AIProvider):
    """
    Safe default provider (no real AI).
    """
    def ask(self, prompt: str) -> str:
        return (
            "AI (dummy): Your system can likely run a disposable VM. "
            "If virtualization is disabled, enable it in BIOS. "
            "If resources are limited, use a lightweight VM profile."
        )
