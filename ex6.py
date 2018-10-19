types_of_people = 10
# this variable is a string that accepts a variable
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "dont't"
# string inside of a string twice
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

# string inside of a string
# 'f' allows you to pass in a string variable as a variable
print("I said: {x}")
# string inside of a string
print(f"I also said: '{y}'")

hilarious = False
# this is a variable that takes a parameter?
joke_evaluation = "Isn't that joke so funny?! {}"

print(f"joke_evaluation")
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# concats two variables that contain strings
print(w + e)
