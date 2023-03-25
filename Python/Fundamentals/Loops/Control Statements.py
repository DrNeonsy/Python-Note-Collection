# Here We Will Take A Look At The Three Keywords "Break" "Continue" "Pass" Which Are Used In Combinations With Loops

# They Are Also Referred To As "Flow Control Statements"

# In The While Loop We Had A Condition That Would Only Allow The Code To Run If The Condition Was True

# So Let's Do The Same But Instead Of Having A Condition That Can Be False, We Define It Inside The Loop

while True:
    name = input("What's Your Name? ")

    if name.count(" ") == len(name) or name == "":
        print("Enter Something Valid...\n")
    else:
        print("Your Name Is: " + name)
        break  # This Will Break Out Of The Loop

# So The "Break" Keyword Will Break Out Of The Loop

# The "Continue" Keyword Will Skip The Current "Iteration" Of The Loop Or In Other Words

# Skip The Rest Of The Loops Code And Return To The Top

for i in range(1, 11):
    if (i % 2 == 0):  # The "%" Is Called The Modulus Operator And It Will Return The Remainder Of The Division
        continue  # So If A Number Can Be Divided By 2 Without A Remainder, It Will Be Even
    print(i)

# Now Python Has Something Interesting Called "Pass" Which Is Used To "Pass" Over The Code

# If You Have An Empty Loop Or Condition, Python Will Throw An Error, However If You Use "Pass"

# It Will Be Treated As A Placeholder And The Code Will Run Without Any Errors

for i in range(1, 11):
    if (i % 2 == 0):
        pass  # So This Will Not Do Anything
    else:
        print(i)
