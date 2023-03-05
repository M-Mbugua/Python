# Python 3.10.1
# Encoding UTF-8
# Program to tell whether a given number is even or odd.


number = int(input("Please enter a number between 1 and 1000: "))


# Function to check whether the number is even or odd
def even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even.")

    else:
        print(f"{num} is odd.")


# Checks to ensure that user input meets requirements
if number < 0 or number > 1000:
    number = int(input("The number you entered is not less than or equal to 10000.\nPlease try again: "))
    even_odd(number)

else:
    even_odd(number)

# Second
# if number < 0 or number > 1000:
#     number = int(input("Please enter a number between 1 and 1000: "))
#
#     if number % 2 == 0:
#         print(f"{number} is even.")
#
#     else:
#         print(f"{number} is odd.")
#
# else:
#     if number % 2 == 0:
#         print(f"{number} is even.")
#
#     else:
#         print(f"{number} is odd.")





