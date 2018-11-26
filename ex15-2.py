from sys import argv

script = argv

userfile = input("What is the filename?")
txt = open(userfile)

print(f"Here's your file {userfile}:")

print(txt.read())

txt.close()
