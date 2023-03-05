# Python 3.10.1
# Encoding UTF-8
# Guessing game where a random number is generated and the player has three
# tries to guess. If they do not, they lose and the game ends.

import random


# Generate a random number
random_number = random.randint(0, 9)
# Ensure that the number generated is constant throughout the game
secret_number = random_number

# for loop
for attempts in range(3):
    # Cast guess to integer because the input takes string data type
    guess = int(input("Please type your lucky number: "))

    # Correct guess condition
    if guess == secret_number:
        print("Congratulations!!! You win.")
        break

    # Wrong guess condition
    elif attempts >= 0:
        print("Please try again")

# Tries have been exhausted
else:
    print(f"You lose. The secret number is {secret_number}.")


# while loop
# attempts = 0
# while attempts < 3:
#     # Cast guess to integer because the input takes string data type
#     guess = int(input("Please type your lucky number: "))
#     attempts = attempts + 1
#
#     # Correct guess condition
#     if guess == secret_number:
#         print("Congratulations!!! You win.")
#         break
#
#     # Wrong guess condition
#     elif attempts >= 0:
#         print("Please try again")
#
# # Tries have been exhausted
# else:
#     print(f"You lose. The secret number is {secret_number}.")
