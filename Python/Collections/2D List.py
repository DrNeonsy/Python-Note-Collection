# A 2D List Is A List Of Lists Or In Other Words A List That Groups Other Lists Together

reds = ["red", "wine red", "dark red", "light red", "pink red"]
greens = ["green", "dark green", "light green", "blue green"]
blues = ["blue", "dark blue", "light blue", "sky blue", "navy blue"]

colors = [reds, greens, blues]  # This Is A 2D List

# print(colors) # Prints The Whole Collection

print(colors[0])  # Prints The First List In The Collection

# Prints The First Item In The First List In The Collection
print(colors[0][0])

# Len Returns The Number Of Lists In The Collection
print(len(colors))

# Therefore To Get The Number Of Items In The First List We Must Use The Len Function On An Index
print(len(colors[0]))

# So Accessing An Element Still Works The Same
# But In This Case We Have To Specify The List And The Item With 2 Indexes
