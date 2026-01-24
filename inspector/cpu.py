"""
cpu.py
System CPU inspection utilities.

Responsibilities:
- Parse CPU information text
- Detect CPU vendor
- Detect hardware virtualization support (VT-x / AMD-V)

Design notes:
- Parsing logic is isolated for unit testing
- System access is read-only
- No side effects
"""

def parse_cpuinfo(cpuinfo_text: str) -> dict:
    """
    Parse cpuinfo text and detect virtualization support.

    Args:
        cpuinfo_text (str): Contents of /proc/cpuinfo

    Returns:
        dict: {
            "vendor": str,
            "virtualization_supported": bool,
            "virtualization_type": str or None
        }
    """
    text = cpuinfo_text.lower()

    vendor = "Unknown"
    virtualization_supported = False
    virtualization_type = None

    # Detect Intel CPUs
    if "genuineintel" in text or "intel" in text:
        vendor = "Intel"
        if "vmx" in text:
            virtualization_supported = True
            virtualization_type = "VT-x"

    # Detect AMD CPUs
    elif "authenticamd" in text or "amd" in text:
        vendor = "AMD"
        if "svm" in text:
            virtualization_supported = True
            virtualization_type = "AMD-V"

    return {
        "vendor": vendor,
        "virtualization_supported": virtualization_supported,
        "virtualization_type": virtualization_type,
    }


def get_cpu_info() -> dict:
    """
    Read /proc/cpuinfo from the system and parse it.

    Returns:
        dict: Parsed CPU information
    """
    try:
        with open("/proc/cpuinfo", "r") as f:
            cpuinfo_text = f.read()
        return parse_cpuinfo(cpuinfo_text)

    except FileNotFoundError:
        return {
            "vendor": "Unsupported OS",
            "virtualization_supported": False,
            "virtualization_type": None,
        }


if __name__ == "__main__":
    info = get_cpu_info()
    for key, value in info.items():
        print(f"{key}: {value}")

