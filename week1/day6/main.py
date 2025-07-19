# Tip Calculator
def calculate_tip(amount, percent):
    return amount * (percent / 100)

total = float(input("Bill amount: "))
tip_percent = float(input("Tip %: "))
print(f"Tip: ₹{calculate_tip(total, tip_percent):.2f}")

# Global Counter
counter = 0

def increment():
    global counter
    counter += 1

for _ in range(5):
    increment()
print("Global Counter:", counter)
