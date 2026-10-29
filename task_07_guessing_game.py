# NUMBER GUESSING GAME
secret_number = 7
guess = int(input("Guess the number: "))
while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Try again: "))
print("Correct! You found the number.")

"""
# ----- Challenge 1 -----
secret_number = 7
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("Congratulations!")
        print("You guessed the number in", attempts, "attempts.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
        # ----- Challenge 2 -----
        secret_number = 7
max_attempts = 5
attempts = 0
guess = 0

while attempts < max_attempts:
    guess = int(input("Guess the number: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("Congratulations!")
        print("You guessed the number in", attempts, "attempts.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

if guess != secret_number:
    print("Game Over!")
    print("The number was", secret_number)
    """