import random
import sys


def get_random_number():
    return random.randrange(0, 100)


def get_user_number():
    return int(input("Enter your guess: "))


def play_again():
    return input("play again (y/n)?  ")


secrete_number = random.randrange(0, 100)
guess = None
# while True:
# if guess == secrete_number:
#     print("Done!")
#     break
while guess != secrete_number:
    guess = int(input("enter: "))
    if guess > secrete_number:
        print("to big")
        continue
    elif guess < secrete_number:
        print("to small")
        continue
    else:
        print("Done!")
        play_again = input("play again? (y/n)? ")
        if play_again.lower().startswith("y"):
            guess = int(input("enter: "))
            continue
        else:
            sys.exit()
