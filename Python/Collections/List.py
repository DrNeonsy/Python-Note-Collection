# A List Is Used To Store Multiple Items In A Single Variable
colors = ["blue", "aqua", "teal", "lightblue", "night blue"]

# As We Have Learned With Strings, An Index Always Starts At 0 So To Access The First Element
# We Have To Use The Index 0 On The Collection Variable Name That Is Holding The Element
print(colors[0])

# If Output | Printing Works Like That Then So Does Input | Changing The Value Of An Element

print(colors[4])
colors[4] = "dark blue"
print(colors[4])

# Loops Can Be Useful To "Iterate" Through A Collection Like A String Or In This Case A List

print()
for element in colors:
    print(element)

print()

# We Can Also Dynamically Add Elements To The End Of A List
colors.append("deep blue")

# We Can Also Remove An Element By It's Value
colors.remove("blue")

# We Can Also "pop" The Last Element Off The List | This Is The Default Behavior Of The Pop Method
# You Could Also Specify The Index Of An Element You Want To Remove
colors.pop()

# In Contrast To Append We Can Also Insert An Element At A Specific Index

# Now Blue Is Back At The Beginning Of The List After We Were So Cruel To Remove It
colors.insert(0, "blue")

# To Get The Size Of A Collection Like A List You Can Use The Previous Shown Len Function
print(len(colors))

# We Can Also Sort The List Which In This Case Is Alphabetical
colors.sort()
print(colors)

# You Can Reverse The Order Of The List With The Reverse Method
colors.reverse()
print(colors)

# We Can Also Join Two Lists Together With The

moreBluesColors = ["navy", "aquamarine", "royal blue", "sky blue"]

combinedList = colors + moreBluesColors
# You Could Also Use The Extend Method

# combinedList = colors.copy()
# combinedList.extend(moreBluesColors)

combinedList.sort()

print()
print("Combined List: ", combinedList)
print()

# To Remove All Elements From A List We Can Use The Clear Method
colors.clear()
print(colors)
