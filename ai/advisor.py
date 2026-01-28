
"""
advisor.py
AI advisor that explains system results and suggests next steps.

This module does NOT execute commands.
"""

from ai.provider import AIProvider


def build_prompt(summary: dict) -> str:
    return f"""
You are a Linux virtualization assistant.

System summary:
- CPU vendor: {summary['cpu_vendor']}
- Virtualization supported: {summary['virt']}
- Total RAM (GB): {summary['ram_gb']}
- Free disk (GB): {summary['disk_free_gb']}
- Readiness status: {summary['status']}
- Reasons: {summary['reasons']}

Host operating system:
- ID: {summary["os_id"]}
- Name: {summary["os_name"]}

TASK:
Create a COMPLETE, SAFE plan to set up virtualization and launch a DISPOSABLE
browsing virtual machine on this system.

Rules:
- Use the correct package manager for the OS.
- Do NOT execute anything.
- The VM must NOT persist any data.
- The final step must launch a disposable VM using a temporary overlay disk
  that is deleted when the VM exits.

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

Return ONLY the plan in this format.
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
For the final step, use a QEMU command that:
- Creates a temporary qcow2 overlay using mktemp
- Uses a read-only base image at images/debian-base.qcow2
- Deletes the overlay after the VM exits
"""
def get_vm_assist_plan(provider, summary: dict) -> str:
    prompt = build_vm_assist_prompt(summary)
    return provider.ask(prompt)
