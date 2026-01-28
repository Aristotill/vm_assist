
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
def build_vm_assist_prompt(summary: dict) -> str:
    return f"""
You are a Linux virtualization assistant for Fedora.

System summary:
- CPU vendor: {summary['cpu_vendor']}
- Virtualization supported: {summary['virt']}
- Total RAM (GB): {summary['ram_gb']}
- Free disk (GB): {summary['disk_free_gb']}
- Readiness status: {summary['status']}

Return a structured plan in EXACT format below.
Include a final step that launches a DISPOSABLE browsing VM using QEMU/KVM
with a temporary overlay disk that is deleted on VM exit.

FORMAT (do not deviate):

PLAN:
STEP 1:
TITLE: <short title>
REASON: <why this is needed>
COMMAND: <shell command>

STEP 2:
TITLE: ...
REASON: ...
COMMAND: ...

Use Fedora commands.
For the final step, use QEMU with:
- a read-only base image
- a temporary overlay disk
- delete the overlay on exit
"""
def get_vm_assist_plan(provider, summary: dict) -> str:
    prompt = build_vm_assist_prompt(summary)
    return provider.ask(prompt)
