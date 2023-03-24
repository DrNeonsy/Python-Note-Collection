# Defines A Block Of Code That Will Be Executed If The Condition Asked Is True
# It Is A Simple Form Of Conditional Execution Or Decision Making

# There Are Operations Like:

# < Less Than | > Greater Than | == Equal To |!= Not Equal To
# >= Greater Than Or Equal To | <= Less Than Or Equal To

# In Most Languages, You Use {} To Define A Block But In Python You Use Indentation And ":"

price = float(input("Enter Price: "))

print("Your Price Is: ", price)

if price == 5:
    print("Which Is My Favorite Number")
elif price == 5.5:
    print("Which Is Twice My Favorite Number, Literally")
elif price < 5:
    print("Which Is Less Than 5")
else:
    print("Which Is Greater Than 5")

# So The Structure Goes As Followed: If "Condition" Then Do This | Else If That "Condition" Try That... And So On
# Else Or "If None Of The Asked Conditions Are True" Then Do This

# The Order Of Which You Enter These "elif's" Is Important Because The Logical Flow Of Code Goes Top To Bottom
