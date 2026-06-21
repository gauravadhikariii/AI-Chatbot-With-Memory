import json
import os

FILE_PATH = "chats/history.json"


# Agar file exist nahi karti to create karo
def initialize_memory():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as file:
            json.dump([], file)


# History load karo
def load_history():
    initialize_memory()

    with open(FILE_PATH, "r") as file:
        return json.load(file)


# History save karo
def save_history(history):
    with open(FILE_PATH, "w") as file:
        json.dump(history, file, indent=4)


# Ek message add karo
def add_message(message):
    history = load_history()
    history.append(message)
    save_history(history)


# History return karo
def get_history():
    return load_history()


# History clear karo
def clear_history():
    save_history([])