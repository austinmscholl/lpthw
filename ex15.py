# imports the 'argv' module from 'sys' library
from sys import argv

# argv accepts 2 arguments, script and filename
script, filename = argv

# opens filename and returns a corresponding file object
# assigns that file object to the variable txt
txt = open(filename)

# prints a string with the filename
print(f"Here's your file {filename}:")
# prints the result of the .read() method called on the txt variable
print(txt.read())
# frees system resources
txt.close()

# prints a string
print("Type the the filename again:")
# prompts the user for input and assigns it to variable file_again
file_again = input("> ")

# opens file_again and returns a corresponding file object
# assigns that file object to the variable txt_again
txt_again = open(file_again)

# prints the results of the .read() method on the txt_again variable
print(txt_again.read())

## frees up system resources
# txt_again.close()
