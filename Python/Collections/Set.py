# So What Is A Set? A Set Is A Collection Of Items That Are Unordered And Therefore Have No Index
# It Also Does Not Allow For Duplicate Items Unlike A List Or Tuple (They Will Be Ignored)

# While You Cannot Change A Value, You Can Still Add And Remove Items From A Set

aSet = {"blue", "aqua", "teal", "lightblue", "night blue"}

# Seeing That We Have No Index, The Only Way We Get All Items Is Via A Loop
print("Set: ")

for color in aSet:
    print(color)

print()

# You Can Add Items To A Set Using The Add Method Or Combine By Using The Update Method
print("Added \"Deep Blue\": ")

aSet.add("deep blue")  # Adds The Item To The Set
for color in aSet:
    print(color)

print()

aTuple = ("navy", "aquamarine", "royal blue", "sky blue")

aSet.update(aTuple)  # Adds The Items From The Tuple To The Set

print("Added Tuple To The Set: ")

aSet.add("deep blue")
for color in aSet:
    print(color)

print()

# You Can Also Use Union To Combine Sets Which Will Return A New Set As A Result

# Returns A New Set With The Items From Both The Set And Tuple
newSet = aSet.union(aTuple)

print("Combined Set And Tuple Via Union: ")

aSet.add("deep blue")
for x in newSet:
    print(x)

print()

# You Can Also "Copy", "Clear" And "Remove" From Sets
