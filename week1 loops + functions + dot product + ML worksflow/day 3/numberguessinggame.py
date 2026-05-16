"""
Number guessing game
Set a secret number = 7 (fixed).
Use a while loop: keep asking user to guess until they get it right.
Print "Too high", "Too low", or "Correct! You got it in X tries
"""
secret = 7
tries = 0

while True:
    guess = int(input("Enter your guess: "))
    tries += 1

    if guess > secret:
        print("Too high")

    elif guess < secret:
        print("Too low")

    else:
        print(f"Correct! You got it in {tries} tries")
        break