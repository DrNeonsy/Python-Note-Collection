# Another Way To Collect Multiple Items In A Single Variable Is With A Tuple

# A Usual Work Case For Tuples Is When You Have A Collection Of Items That You Do Not Want To Change
# And The Data Should "Belong Together"

# A Tuple Is Almost Identical To A List Except That It Is "Immutable" Which Means
# That You Cannot Change It After It Has Been Created

tupleExample = ("blue", "aqua", "teal", "lightblue", "night blue")

print(tupleExample[0])  # The Access Works The Same As It Does With Lists

# So I Just Told You That You Cannot Change Tuples, Well You Can But You Need A List To Do So
# Seeing That They Are Almost Identical To Lists If You Need To Change A Tuple, You Might Better Be Of Using A List

aList = list(tupleExample)
aList.append("deep blue")
tupleExample = tuple(aList)

# So You Create A List, Cast The Tuple To A List, Add An Element, And Cast The List Back To A Tuple
print(tupleExample)

# A Tuple Has Two Methods Which Are "Count" And "Index"

# Count Gives You The Amount Of Times An Element Appears In The Tuple

# Index Gives You The Index Of The First Occurrence Of The Element

# You Can Join A Tuple With Another Tuple Using The + Operator (Example In The List Section)
