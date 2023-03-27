# Unpacking Is A Way Of Assigning Values To Variables From A Sequence Or Collection

# These Are A Few Types I Know Of That Can Be Unpacked: Strings, Lists, Tuples, Dictionaries And Sets

aList = ["blue", "aqua", "teal", "lightblue", "night blue"]

aTuple = ("banana", "apple", "orange", "grape", "strawberry")

# Now To Unpack The List And Tuple Into Variables You Can Write The Following:

(element1, element2, element3, element4, element5) = aList

print(element1)
print(element2)
print(element3)
print(element4)
print(element5)

print()

(fruit1, fruit2, fruit3, fruit4, fruit5) = aTuple

print(fruit1)
print(fruit2)
print(fruit3)
print(fruit4)
print(fruit5)

print()

# If You Unpack A Tuple "Dunno If It Works With Lists" Into Variables
# And You Do Not Want To Use All The Variables You Can Use The * Operator

(fruit1, *fruits, fruit5) = aTuple
# The Order Is Still Important But You Can Use The * Operator To Ignore The Middle Elements (In This Case)
# The * Operator Is Called The "Splat" Operator And It Is Used To "Splat" The Elements Into A List
# Because We Unpack The First And Last Element Into Variables The Middle One With "*" Gets Splatted Into A List

print(fruit1)
print(fruits)
print(fruit5)