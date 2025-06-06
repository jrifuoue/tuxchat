# main.py

# The base script of tuxchat! Search user input in database and print answer! Also can save single key in memory.txt and run simple commands.

import time
import memory
import database
import difflib

def type_writer(text): # type: ignore
    for char in text: # type: ignore
        print(char, end='', flush=True) # type: ignore
        time.sleep(0.03)
    print()

def correct_spelling(input_text): # type: ignore
    words = list(database.RESPONSES.keys())
    matches = difflib.get_close_matches(input_text, words, n=1, cutoff=0.6) # type: ignore
    if matches:
        return matches[0] # type: ignore
    return input_text # type: ignore

def process_input(user_input): # type: ignore
    user_input = user_input.strip().lower() # type: ignore

    # Handle commands with ///
    if user_input.startswith("///"): # type: ignore
        command = user_input[3:].strip() # type: ignore

        if command.startswith("save "): # type: ignore
            try:
                data = command[5:] # type: ignore
                key, value = data.split(":", 1) # type: ignore
                memory.save_to_memory(key.strip(), value.strip()) # type: ignore
                return f">>> TuxChat: Saved '{key.strip()}' successfully!" # type: ignore
            except ValueError:
                return ">>> TuxChat: Invalid format. Use ///save key:value"

        elif command.startswith("get "): # type: ignore
            key = command[4:].strip() # type: ignore
            return memory.retrieve_from_memory(key) # type: ignore

        elif command.startswith("delete "): # type: ignore
            key = command[7:].strip() # type: ignore
            return memory.delete_from_memory(key) # type: ignore

        elif command == "help":
            return ">>> TuxChat: Commands available: ///save key:value | ///get key | ///delete key | ///help | ///exit"  # type: ignore

        elif command == "exit":
            return "exit"

        else:
            return ">>> TuxChat: Unknown command."

    # Try to match corrected spelling
    corrected = correct_spelling(user_input) # type: ignore
    for key in database.RESPONSES:
        if corrected in key:
            response = database.RESPONSES[key]
            return f">>> TuxChat: {response[0]}"

    # Math calculations
    if "+" in user_input or "-" in user_input or "*" in user_input or "/" in user_input:
        try:
            result = eval(user_input) # type: ignore
            return f">>> TuxChat: The result is {result}"
        except Exception:
            return ">>> TuxChat: I couldn't understand that calculation."

    # Default response
    return ">>> TuxChat: Sorry, I didn't understand that."

def main():
    print(">>> TuxChat is ready. Start chatting!")
    while True:
        user_input = input("You: ")
        response = process_input(user_input)
        if response == "exit":
            type_writer(">>> TuxChat: Goodbye!")
            break
        type_writer(response)

if __name__ == "__main__":
    main()
