def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        return f"I {instructions[11:]}"
    elif instructions.endswith("Simon says"):
        ind = instructions.index("Simon says")
        return f"I {instructions[:ind-1]}"
    else:
        return "I won't do it!"
