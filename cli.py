"""
cli.py
Command-line interface for VM-Assist (v0.1).

Purpose:
- Run system inspection
- Display CPU virtualization readiness
"""

from inspector.cpu import get_cpu_info


def main():
    print("VM-Assist — System Inspection (v0.1)\n")

    cpu_info = get_cpu_info()

    print("CPU Information")
    print("----------------")
    print(f"Vendor: {cpu_info['vendor']}")
    print(f"Virtualization Supported: {cpu_info['virtualization_supported']}")
    print(f"Virtualization Type: {cpu_info['virtualization_type']}")


if __name__ == "__main__":
    main()

