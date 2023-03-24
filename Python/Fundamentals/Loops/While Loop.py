# One Of The "Head Controlled Loops" Which Is Executing Code As Long As It's Condition Remains True
# Because It's "Head Controlled" (The Conditions Comes Before The Code Block)
# It'll Only Enter The Code Block If The Condition Is True Otherwise It'll Be Skipped

# A Basic Example Is If Someone Is Suppose To Enter Something (This Will Not Prevent "Only Whitespace")

# name = ""

# while len(name) == 0:
#     name = input("What's Your Name? ")

# A Better Way To Have A Defined But Truly Empty Variable Would Be:

name = None

while not name:
    name = input("What's Your Name? ")

if name.count(" ") == len(name):
    print("You Spammed Spaces :/")
else:
    print("Your Name Is: " + name)
