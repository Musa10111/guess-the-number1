import random
import sys


start_range_number = None
end_range_number = None
guess = None

# get from user/player start and end number
while start_range_number == None and end_range_number == None:
    try:
        start_range_number = int(input('enter the number you want to start: '))
        end_range_number = int(input('enter the number you want to end: '))

        if start_range_number > end_range_number:
            print("start number must be greater than end number.")
            start_range_number = None
            end_range_number = None

    except ValueError:
        print("you must enter an integer value")
        start_range_number = None
        end_range_number = None

# generate random secrete number
secret_number = random.randrange(start_range_number, end_range_number)

# start game
while guess != secret_number:
    try:
        guess = int(input("enter your guess: "))
    except ValueError:
        print("you must enter an integer value.")
    if guess > secret_number:
        print("your guess to big.")
        continue
    elif guess < secret_number:
        print("your guess to small")
        continue
    else:
        print("You win!!")
        sys.exit()
