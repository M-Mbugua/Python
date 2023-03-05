# Python 3.10.1
# Encoding UTF-8
# Guessing game where a random number is generated and the player has five
# tries to guess the random number.

import random


# Generate a random number
random_number = random.randint(0, 50)
# Ensure that the number generated is constant throughout the game
secret_number = random_number

# for loop
# for attempts in range(5):
#     # Cast guess to integer because the input takes string data type
#     guess = int(input("Please enter a number between 0 and 50: "))
#
#     if guess == secret_number:
#         print("Congratulations!!! You guessed correctly.")
#         break
#
#     elif guess > secret_number:
#         print("Sorry, the number you guessed is too high.\nPlease try again. ")
#
#     elif guess < secret_number:
#         print("Sorry, the number you guessed is too low.\nPlease try again. ")

# Tries have been exhausted
# else:
#     print("You're out of tries. The number was", secret_number, ".\nBetter luck next time!")


# while loop
attempts = 0
while attempts < 5:
    # Cast guess to integer because the input takes string data type
    guess = int(input("Please enter a number between 0 and 50: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("Congratulations!!! You guessed correctly.")
        break

    elif guess > secret_number:
        print("Sorry, the number you guessed is too high.\nPlease try again. ")

    elif guess < secret_number:
        print("Sorry, the number you guessed is too low.\nPlease try again. ")

# Tries have been exhausted
else:
    print("You're out of tries. The number was", secret_number, ".\nBetter luck next time!")
