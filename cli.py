"""
cli.py
VM-Assist CLI (v0.4 with optional BYO-AI advisor).

Usage:
  python cli.py
  python cli.py --ai
"""

import sys
from ai.plan_parser import parse_plan
from ai.advisor import get_vm_assist_plan
from actions.executor import ask_and_execute
from ai.advisor import extract_command_from_ai
from inspector.cpu import get_cpu_info
from inspector.ram import get_ram_info
from inspector.disk import get_disk_info
from rules.readiness import evaluate_readiness
from ai.openai_provider import OpenAIProvider
from ai.provider import DummyProvider
from ai.advisor import get_ai_advice
from inspector.os import get_os_info



def main():
    use_ai = "--ai" in sys.argv

    print("VM-Assist — System Readiness Check\n")

    cpu_info = get_cpu_info()
    ram_info = get_ram_info()
    disk_info = get_disk_info()
    os_info = get_os_info()

    readiness = evaluate_readiness(cpu_info, ram_info, disk_info)

    print("System Summary")
    print("--------------")
    print(f"CPU Vendor: {cpu_info['vendor']}")
    print(f"Virtualization Supported: {cpu_info['virtualization_supported']}")
    print(f"Total RAM: {ram_info['total_ram_gb']} GB")
    print(f"Free Disk Space: {disk_info['free_gb']} GB")
    print()

    print("VM Readiness")
    print("------------")
    print(f"Status: {readiness['status']}")
    for reason in readiness["reasons"]:
        print(f" - {reason}")

    if use_ai:
    print("\nAI Advisor")
    print("----------")

    plan_text = get_vm_assist_plan(provider, summary)

    print("\nPROPOSED PLAN")
    print("-------------")
    print(plan_text)

    steps = parse_plan(plan_text)

    mode = input("\nAutomate this plan? (YES/no): ").strip()
    automate = (mode == "YES")

    for i, step in enumerate(steps, start=1):
        print(f"\nSTEP {i}: {step.get('title', '')}")
        print(f"Reason: {step.get('reason', '')}")
        print(f"Command:\n{step.get('command', '')}")

        choice = input("Execute this step? (YES/no): ").strip()
        if choice == "YES":
            ask_and_execute(step["command"])
        else:
            print("Skipped.")
            if automate:
                print("Automation stopped by user.")
                break

        summary = {
            "cpu_vendor": cpu_info["vendor"],
            "virt": cpu_info["virtualization_supported"],
            "ram_gb": ram_info["total_ram_gb"],
            "disk_free_gb": disk_info["free_gb"],
            "status": readiness["status"],
            "reasons": readiness["reasons"],
        }
        summary["os_id"] = os_info["id"]
        summary["os_name"] = os_info["name"]
        try:
            provider = OpenAIProvider()
            print("(Using real BYO-AI provider)\n")
        except Exception as e:
            provider = DummyProvider()
            print(f"(Falling back to dummy AI: {e})\n")

        advice = get_ai_advice(provider, summary)
        print(advice)

        command = extract_command_from_ai(advice)
        if command:
          ask_and_execute(command)



if __name__ == "__main__":
    main()
