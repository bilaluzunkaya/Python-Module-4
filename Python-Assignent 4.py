"""""
Answer1

number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

 Answer2

while True:
    inches = float(input("Enter length in inches (negative value to quit): "))

    if inches < 0:
        print("Program ended.")
        break

    cm = inches * 2.54
    print(f"{inches:.1f} inches is {cm:.2f} centimeters")

Answer3

numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    numbers.append(float(user_input))

if numbers:
    print(f"Smallest number: {min(numbers)}")
    print(f"Largest number: {max(numbers)}")

 Answer4

yimport random

target = random.randint(1, 10)
guess = 0

while guess != target:
    guess = int(input("Guess a number (1-10): "))

    if guess > target:
        print("Too high")
    elif guess < target:
        print("Too low")
    else:
        print("Correct")

Answer5
attempts = 0
correct_user = "python"
correct_pass = "rules"

while attempts < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_user and password == correct_pass:
        print("Welcome")
        break
    else:
        attempts += 1
        if attempts < 5:
            print("Incorrect username or password. Please try again.")
        else:
            print("Access denied")
Answer6
import random

N = int(input("How many random points to generate: "))
n = 0
iterator = 0

while iterator < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n += 1

    iterator += 1

pi_approximation = 4 * n / N
print(f"Approximation of pi: {pi_approximation}")
