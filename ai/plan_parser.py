def parse_plan(text: str):
    steps = []
    current = {}

    for line in text.splitlines():
        line = line.strip()
        if line.startswith("STEP"):
            if current:
                steps.append(current)
            current = {}
        elif line.startswith("TITLE:"):
            current["title"] = line.replace("TITLE:", "").strip()
        elif line.startswith("REASON:"):
            current["reason"] = line.replace("REASON:", "").strip()
        elif line.startswith("COMMAND:"):
            current["command"] = line.replace("COMMAND:", "").strip()

    if current:
        steps.append(current)

    return steps
