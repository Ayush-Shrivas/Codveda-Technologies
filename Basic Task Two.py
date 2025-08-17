import random

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7  # You can change this

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
else:
    print(f"Sorry! You've used all attempts. The number was {secret_number}.")

