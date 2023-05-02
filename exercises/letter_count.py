# Python 3.10.1
# Encoding UTF-8
# program to count the number of words

word = input("What's on your mind today? ")

count = 0

for i in range(len(word)):
    count = count + 1

# print("Fantastic!!! You just told me what's on your mind in ", count, " letters!")
print(f"Fantastic!!! You just told me what's on your mind 
in {count} letters!")
