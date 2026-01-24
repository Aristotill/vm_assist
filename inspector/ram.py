"""
ram.py
System RAM inspection utilities.

Responsibilities:
- Parse memory information
- Report total system RAM
- Provide VM suitability hints (raw data only)

Design notes:
- Parsing logic is isolated for unit testing
- System access is read-only
"""

def parse_meminfo(meminfo_text: str) -> dict:
    """
    Parse /proc/meminfo text and extract total RAM.

    Args:
        meminfo_text (str): Contents of /proc/meminfo

    Returns:
        dict: {
            "total_ram_kb": int,
            "total_ram_gb": float
        }
    """
    total_kb = 0

    for line in meminfo_text.splitlines():
        if line.lower().startswith("memtotal"):
            parts = line.split()
            total_kb = int(parts[1])
            break

    total_gb = round(total_kb / (1024 * 1024), 2) if total_kb else 0.0

    return {
        "total_ram_kb": total_kb,
        "total_ram_gb": total_gb
    }


def get_ram_info() -> dict:
    """
    Read /proc/meminfo from the system and parse it.

    Returns:
        dict: Parsed RAM information
    """
    try:
        with open("/proc/meminfo", "r") as f:
            meminfo_text = f.read()
        return parse_meminfo(meminfo_text)

    except FileNotFoundError:
        return {
            "total_ram_kb": 0,
            "total_ram_gb": 0.0
        }


if __name__ == "__main__":
    info = get_ram_info()
    print(f"Total RAM: {info['total_ram_gb']} GB")

