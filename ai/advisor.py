"""
advisor.py
AI advisor that generates structured plans.

This module does NOT execute commands.
"""

from ai.provider import AIProvider


def build_vm_assist_prompt(summary: dict) -> str:
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
- ID: {summary['os_id']}
- Name: {summary['os_name']}

TASK:
Create a COMPLETE, SAFE plan to set up virtualization and launch a DISPOSABLE
browsing virtual machine on this system.

Rules:
- Use the correct package manager for the OS.
- Do NOT execute anything.
- The VM must NOT persist any data.
- The final step must launch a disposable VM using QEMU/KVM.
- Use a temporary qcow2 overlay created with mktemp.
- Use a read-only base image at images/debian-base.qcow2.
- Delete the overlay automatically when the VM exits.

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


def get_vm_assist_plan(provider: AIProvider, summary: dict) -> str:
    prompt = build_vm_assist_prompt(summary)
    return provider.ask(prompt)

