# Python 3.10.1
# Encoding UTF-8
# Finding the acronym of a word


# First function to create acronym
def acronym_maker(word):
    # Add first letter
    output = word[0]

    # If there is an empty space before a letter then add it to the acronym
    for i in range(1, len(word)):
        if word[i - 1] == ' ':
            output += word[i]

    output = output.end()
    return output


# Takes user input
acronym = input("What phrase would you like to have shortened? ")
print(acronym_maker(acronym))


# Second function to create acronym
def acronym_creator(phrase):
    # Get all words
    lst = phrase.split()
    output1 = ""

    # Iterate over words
    for word in lst:
        # Get first letter of each word
        output1 += word[0]

    # Convert each letter to uppercase
    output1 = output1.upper()
    return output1


# Take user input
input1 = input("What phrase would you like to have shortened? ")
print(acronym_creator(input1))
