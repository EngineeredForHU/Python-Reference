# Examples of writing/opening to a file in python
# For a more comprehensive explanation head to:
# https://www.geeksforgeeks.org/python/file-handling-python/

# This is a basic example, for a more practical example head to: withopen_file_example.py

# Running this file will create a file in the current working directory
# Just be aware!


# There are 5 modes. (creating, opening, reading, writing, and closing)
# The file variable opens the 'data.txt' with the writing mode indicated by the 'w'.
file = open('data.txt','w')
# We then run the file variable with .write() to write the things we want
file.write('Hello\n')


print(f'Mode: {file.mode}')