# Python 3.10.1
# Encoding UTF-8
# The program checks whether user input is a palindrome.


print("A palindrome is a number or string that remains the same when reversed.")


# Takes user input
test_number = input("\nEnter a number to find out whether it is a palindrome: ")


# Using str() + string slicing
# for checking a number is palindrome
res = str(test_number) == str(test_number)[::-1]


# Printing result
print("Is it a palindrome? : " + str(res))


# Takes user input
def isPalindrome(s):
    return s == s[::-1]


# Driver code
word = input("\nEnter a word to find out whether it is a palindrome: ")
result = isPalindrome(word)


if result:
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")
