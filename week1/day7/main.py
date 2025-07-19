# Daily Journal
with open("journal.txt", "a") as file:
    entry = input("Write your journal entry: ")
    file.write(entry + "\n")
    print("Entry saved.")

# Contact Manager CLI
import json

try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {}

name = input("Enter name: ")
phone = input("Enter phone number: ")
contacts[name] = phone

with open("contacts.json", "w") as f:
    json.dump(contacts, f, indent=2)

print("Contact saved.")
