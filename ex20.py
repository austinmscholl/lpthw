# imports sys module from argv library
from sys import argv

# argv accepts two parameters
script, input_file = argv

# defines a function that accepts one (file) argument
def print_all(f):
    # prints the contents of the file
    print(f.read())

# defines a function called rewind that resets the current file position to 0
def rewind(f):
    f.seek(0)

# defines a function that accepts 2 arguments, a line number and a file
def print_a_line(line_count, f):
    # prints a line from a file
    print(line_count, f.readline())

# opens a file and assigns it to variable 'current_file'
current_file = open(input_file)

# prints a string
print("First let's print the whole file:\n")

# prints the whole file plus a new line
print_all(current_file)

# prints a string
print("Now let's rewind, kind of like a tape.")

# resets the file position(in bytes) to 0 by passing the file 'current_file'
# as a parameter to the funtion 'rewind()'
rewind(current_file)

# prints a string
print("Let's print three lines: ")

# assigns the variable 'current_line' a value of 1
current_line = 1
# calls a function that accepts 2 parameters
print_a_line(current_line, current_file)

# increments the variable 'current_line' by 1
current_line+=1
print_a_line(current_line, current_file)

# increments the variable 'current_line' by 1
current_line = current_line + 1
print_a_line(current_line, current_file)
