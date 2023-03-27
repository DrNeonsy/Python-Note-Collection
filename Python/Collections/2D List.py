# A 2D List Is A List Of Lists Or In Other Words A List That Groups Other Lists Together

reds = ["red", "wine red", "dark red", "light red", "pink red"]
greens = ["green", "dark green", "light green", "blue green"]
blues = ["blue", "dark blue", "light blue", "sky blue", "navy blue"]

colors = [reds, greens, blues]  # This Is A 2D List

# print(colors) # Prints The Whole Collection

print(colors[0])  # Prints The First List In The Collection

# Prints The First Item In The First List In The Collection
print(colors[0][0])

# So Accessing An Element Still Works The Same
# But In This Case We Have To Specify The List And The Item With 2 Indexes
