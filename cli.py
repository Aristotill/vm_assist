"""
cli.py
Command-line interface for VM-Assist (v0.3).

Purpose:
- Run system inspection
- Evaluate VM readiness
- Display clear summary
"""

from inspector.cpu import get_cpu_info
from inspector.ram import get_ram_info
from inspector.disk import get_disk_info
from rules.readiness import evaluate_readiness


def main():
    print("VM-Assist — System Readiness Check (v0.3)\n")

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
    print("Reasons:")
    for reason in readiness["reasons"]:
        print(f" - {reason}")


if __name__ == "__main__":
    main()
