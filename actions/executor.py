"""
executor.py
Permission-gated command execution.

Nothing runs unless the user explicitly approves.
"""

import subprocess


def ask_and_execute(command: str):
    """
    Ask the user for permission before executing a command.

    Args:
        command (str): Shell command to execute
    """
    print("\nAI-suggested command:")
    print("---------------------")
    print(command)

    choice = input("\nDo you want to execute this command? (YES/no): ").strip()

    if choice == "YES":
        print("\nExecuting command...\n")
        subprocess.run(command, shell=True, check=False)
    else:
        print("\nExecution cancelled by user.")
