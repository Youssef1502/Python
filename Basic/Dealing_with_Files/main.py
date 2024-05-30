#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python code to explain how we can deal with the text files.
================================================================================'''

# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, this is a line of text.\n")
    file.write("Here is another line.\n")
    file.writelines(["Line 3\n", "Line 4\n"])

print("Data written to 'example.txt'.")

# Reading from the file
with open('example.txt', 'r') as file:
    # Reading the entire file content
    content = file.read()
    print("Reading entire file content:\n", content)
    
    print("---------------------------------\n")
    # Resetting the file pointer to the beginning
    file.seek(0)
    
    # Reading line by line
    print("Reading file line by line:")
    line = file.readline()
    while line:
        print(line, end='')  # 'end' is used to avoid double newlines
        line = file.readline()

    print("\n---------------------------------\n")

    # Resetting the file pointer to the beginning
    file.seek(0)
    
    # Reading all lines into a list
    lines = file.readlines()
    print("Reading all lines into a list:\n", lines)

# Appending to a file
with open('example.txt', 'a') as file:
    file.write("Appending a new line at the end.\n")

print("\n---------------------------------\n")

print("Appended data to 'example.txt'.")

# Reading the updated file content
with open('example.txt', 'r') as file:
    updated_content = file.read()
    print("\nUpdated file content:\n", updated_content)
