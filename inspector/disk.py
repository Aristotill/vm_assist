
"""
disk.py
System disk inspection utilities.

Responsibilities:
- Detect available disk space on the root filesystem
- Report free disk in GB

Design notes:
- Uses standard library only
- Read-only
- Linux-safe (Fedora compatible)
"""

import shutil


def get_disk_info(path: str = "/") -> dict:
    """
    Get disk usage statistics for a given path.

    Args:
        path (str): Filesystem path to inspect (default: root)

    Returns:
        dict: {
            "total_gb": float,
            "used_gb": float,
            "free_gb": float
        }
    """
    usage = shutil.disk_usage(path)

    total_gb = round(usage.total / (1024 ** 3), 2)
    used_gb = round(usage.used / (1024 ** 3), 2)
    free_gb = round(usage.free / (1024 ** 3), 2)

    return {
        "total_gb": total_gb,
        "used_gb": used_gb,
        "free_gb": free_gb
    }


if __name__ == "__main__":
    info = get_disk_info()
    print(f"Disk Total: {info['total_gb']} GB")
    print(f"Disk Used: {info['used_gb']} GB")
    print(f"Disk Free: {info['free_gb']} GB")
