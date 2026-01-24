"""
cli.py
Command-line interface for VM-Assist (v0.2).

Purpose:
- Run system inspection
- Display CPU and RAM readiness
"""

from inspector.cpu import get_cpu_info
from inspector.ram import get_ram_info


def main():
    print("VM-Assist — System Inspection (v0.2)\n")

    cpu_info = get_cpu_info()
    ram_info = get_ram_info()

    print("CPU Information")
    print("----------------")
    print(f"Vendor: {cpu_info['vendor']}")
    print(f"Virtualization Supported: {cpu_info['virtualization_supported']}")
    print(f"Virtualization Type: {cpu_info['virtualization_type']}")
    print()

    print("Memory Information")
    print("------------------")
    print(f"Total RAM: {ram_info['total_ram_gb']} GB")


if __name__ == "__main__":
    main()

