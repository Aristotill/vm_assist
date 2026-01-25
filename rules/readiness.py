
"""
readiness.py
System readiness evaluation rules.

Responsibilities:
- Evaluate CPU, RAM, and Disk inspection data
- Decide VM readiness level
- Explain decision clearly

This module contains NO system access.
"""

def evaluate_readiness(cpu: dict, ram: dict, disk: dict) -> dict:
    """
    Evaluate system readiness for running a disposable VM.

    Args:
        cpu (dict): CPU inspection data
        ram (dict): RAM inspection data
        disk (dict): Disk inspection data

    Returns:
        dict: {
            "status": str,        # READY | LIMITED | NOT_READY
            "reasons": list[str]  # Explanation
        }
    """
    reasons = []
    status = "READY"

    # CPU checks
    if not cpu.get("virtualization_supported"):
        status = "NOT_READY"
        reasons.append("CPU virtualization is not supported or not enabled.")

    # RAM checks
    total_ram = ram.get("total_ram_gb", 0)
    if total_ram < 4:
        status = "NOT_READY"
        reasons.append("Less than 4 GB RAM available.")
    elif total_ram < 8 and status != "NOT_READY":
        status = "LIMITED"
        reasons.append("RAM is below recommended 8 GB.")

    # Disk checks
    free_disk = disk.get("free_gb", 0)
    if free_disk < 20:
        status = "NOT_READY"
        reasons.append("Less than 20 GB free disk space.")
    elif free_disk < 40 and status == "READY":
        status = "LIMITED"
        reasons.append("Disk space is below recommended 40 GB.")

    if not reasons:
        reasons.append("System meets recommended requirements.")

    return {
        "status": status,
        "reasons": reasons
    }
