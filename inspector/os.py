def get_os_info() -> dict:
    info = {"id": "unknown", "name": "Unknown"}

    try:
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("ID="):
                    info["id"] = line.strip().split("=")[1].strip('"')
                elif line.startswith("NAME="):
                    info["name"] = line.strip().split("=")[1].strip('"')
    except FileNotFoundError:
        pass

    return info
