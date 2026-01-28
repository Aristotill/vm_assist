
"""
advisor.py
AI advisor that explains system results and suggests next steps.

This module does NOT execute commands.
"""

from ai.provider import AIProvider


def build_prompt(summary: dict) -> str:
    return f"""
You are a cybersecurity assistant.

System summary:
- CPU vendor: {summary['cpu_vendor']}
- Virtualization supported: {summary['virt']}
- Total RAM (GB): {summary['ram_gb']}
- Free disk (GB): {summary['disk_free_gb']}
- Readiness status: {summary['status']}
- Reasons: {summary['reasons']}

Explain the result in simple terms.
Suggest safe next steps if applicable.
Do NOT execute anything.
If the system is READY, suggest a Fedora command to install QEMU/KVM.
Prefix the command with:
COMMAND:

"""


def get_ai_advice(provider: AIProvider, summary: dict) -> str:
    prompt = build_prompt(summary)
    return provider.ask(prompt)
def extract_command_from_ai(text: str) -> str | None:
    """
    Very simple command extraction.
    Looks for lines starting with: COMMAND:
    """
    for line in text.splitlines():
        if line.startswith("COMMAND:"):
            return line.replace("COMMAND:", "").strip()
    return None
