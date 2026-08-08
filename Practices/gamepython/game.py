import random


def play_game():
    lucky_number = random.randint(1, 50)

    while True:
        guess = int(input("Guess a number between 1 and 50: "))

        if guess == lucky_number:
            print("Congratulations! You guessed the lucky number!")
            break
        elif guess > lucky_number:
            print("Too high! Try again.")
        elif guess < lucky_number:
            print("Too low! Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 50.")

play_game()