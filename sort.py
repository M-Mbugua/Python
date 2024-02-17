# Open file for reading
with open("wordlist.txt", "r") as f:
    # Read the lines until end of file is reached
    names = [line.strip() for line in f.readlines()]

# Sort the strings
names.sort()

# Open the file for writing
with open("wordlist.txt", "w") as f:
    # Insert the sorted strings into the file
    for name in names:
        f.write(name + "\n")

