# Number Guesser
import random
num = random.randint(1, 10)
guess = int(input("Guess a number (1-10): "))
if guess == num:
    print("Correct!")
else:
    print(f"Wrong! The number was {num}")

# Grade Calculator
marks = [75, 80, 65, 90]
average = sum(marks) / len(marks)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "D"
print(f"Average: {average}, Grade: {grade}")
