"""
cli.py
VM-Assist CLI (v0.4 with optional BYO-AI advisor).

Usage:
  python cli.py
  python cli.py --ai
"""

import sys
from inspector.cpu import get_cpu_info
from inspector.ram import get_ram_info
from inspector.disk import get_disk_info
from rules.readiness import evaluate_readiness
from ai.openai_provider import OpenAIProvider
from ai.provider import DummyProvider
from ai.advisor import get_ai_advice


def main():
    use_ai = "--ai" in sys.argv

    print("VM-Assist — System Readiness Check\n")

    cpu_info = get_cpu_info()
    ram_info = get_ram_info()
    disk_info = get_disk_info()

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

        summary = {
            "cpu_vendor": cpu_info["vendor"],
            "virt": cpu_info["virtualization_supported"],
            "ram_gb": ram_info["total_ram_gb"],
            "disk_free_gb": disk_info["free_gb"],
            "status": readiness["status"],
            "reasons": readiness["reasons"],
        }

        try:
            provider = OpenAIProvider()
            print("(Using real BYO-AI provider)\n")
        except Exception as e:
            provider = DummyProvider()
            print(f"(Falling back to dummy AI: {e})\n")

        advice = get_ai_advice(provider, summary)
        print(advice)



if __name__ == "__main__":
    main()
