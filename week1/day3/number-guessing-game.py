import random

number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print("Congratulations! You guessed the correct number in", attempts, "attempts!")
        break
    elif guess < number:
        print("Too low. Try a higher number.")
    else:
        print("Too high. Try a lower number.")
