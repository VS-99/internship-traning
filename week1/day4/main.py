# Phonebook
phonebook = {
    "Alice": "1234567890",
    "Bob": "0987654321"
}
phonebook["Charlie"] = "5556667777"
print("Phonebook:", phonebook)

# Voter Checker
voters = {"A123", "B456", "C789"}
voter_id = input("Enter your voter ID: ")
if voter_id in voters:
    print("You are eligible to vote.")
else:
    print("ID not found.")
