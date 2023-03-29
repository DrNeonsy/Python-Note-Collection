# A Dictionary, Map Or Hash Table Is A Data Structure That Maps Keys To Values
# So Basically It Provides A Paring Of One Datatype With Another For Example Association

# They Are Changeable, Unordered And Do Not Allow Duplicates Like Sets

# In Python This Data Structure Can Mix Datatypes In Any Way You Need

# A Dictionary Is Using { Like Sets } Separating The Keys And Values With A Colon And The Pair With A Comma

aDictionary = {
    "name": "Your Name",
    "age": 22,
    "favColor": "Blue",
    "alive": True
}

print(aDictionary)  # To Print The Entire Dictionary

print(aDictionary["favColor"])  # To Print A Specific Value

aDictionary["favColor"] = "Deep Blue"  # To Change A Value

# You Can Also Use The Update Method To Change A Value

aDictionary["likesDogs": True]  # To Add A New Key And Value

# And Again You Can Use The Update Method To Add A New Key And Value

# To Remove The Last Element You Can Use aDictionary.popitem()

# To Remove A Specific Element You Can Use aDictionary.pop("keyName")

# You Can Also Use The del Keyword To Remove A Specific Element Or The Entire Dictionary

# To Clear It You Can Use aDictionary.clear()

aDictionary.clear()
