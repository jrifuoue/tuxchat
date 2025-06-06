# memory.py

# Simple memory management!

import os

MEMORY_FILE = "memory.txt"

def load_memory(): # type: ignore
    if os.path.exists(MEMORY_FILE):
        memory = {}
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    memory[key.strip()] = value.strip()
        return memory # type: ignore
    return {} # type: ignore

def save_to_memory(key, value): # type: ignore
    memory = load_memory() # type: ignore
    memory[key] = value
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        for k, v in memory.items(): # type: ignore
            f.write(f"{k}: {v}\n")
    print(">>> TuxChat: Something is saved in memory!")

def retrieve_from_memory(key): # type: ignore
    memory = load_memory() # type: ignore
    if key in memory:
        return f">>> TuxChat: The value for '{key}' is: {memory[key]}"
    else:
        return f">>> TuxChat: I don't have anything saved for '{key}'."

def delete_from_memory(key): # type: ignore
    memory = load_memory() # type: ignore
    if key in memory:
        del memory[key]
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            for k, v in memory.items(): # type: ignore
                f.write(f"{k}: {v}\n")
        return f">>> TuxChat: The value for '{key}' has been deleted."
    else:
        return f">>> TuxChat: No such entry found for '{key}'."
