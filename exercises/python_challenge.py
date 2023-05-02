# Python 3.10.1
# Encoding UTF-8
# Program to determine and display prime numbers.
# The output is stored in a separate file.


start = 1
end = 250


for num in range(start, end + 1):
    # All prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            # Create a file in append mode
            try:
                with open('results.txt', 'a') as f:
                    # Convert numbers to string to write into text file
                    # Appends without spacing the numbers.
                    # f.write(str(num))

                    # Convert numbers to string to write into text file
                    # Skips a line before appending
                    data = "\r\n%s" % num
                    f.write(data)

            # If the file could not be created
            except FileNotFoundError:
                print("The file could not be created")