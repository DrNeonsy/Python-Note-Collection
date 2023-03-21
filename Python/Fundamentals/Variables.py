# Variables Are Containers Or Boxes That Can Be Used To Store Data
# There Are Several Types Of Variables: String, Integer, Float, Boolean, List, Dictionary, Tuple, Set And More

# To Create A Variable, You Can Use the following Syntax: A Unique Variable Name, A (=) And The Value You Want To Store

# We'll Start With A String Which Can Be Either In Single Quotes or Double Quotes
# A String Is A Sequence Of Characters Like "Hello World"

text = "My First Python Program"

# To Display Something, You Can Use The print() Function

print(text)

# If You Want To Use The print() Function To Display Something Directly You Can Just Write It

print("This Also Works")

# To Combine Two Strings, You Can Use the + "Operator"

print("This Is " + text)

# To View The Type Of A Variable, You Can Use the type() Function

print(type(text))

# Let's Create Another Variable As A Whole Number Also Known As "Integer"

number = 57
print(number)

# As You Might Expect, You Can Do Math "Operations" With Numbers

# number = number + 10 | This Would Result In 67
# You Can Also Do A Shorthand Operation With Numbers

number += 10
# print("Number: " + number) | You Cannot "Concatenate" A Number With A String
print("Number: " + str(number))

# As You Can See A String Is Part Of The 'str' "Class" And The str() Is Called A Type Cast
# Because We Cast The Number To A String | Another Term Would Be To Convert A Number To A String

print(type(number))

# Let's Have A Look At Floating Point Numbers

realNumber = 7.5
print("Real Number: " + str(realNumber))

print(type(realNumber))

# Another Basic / Often Used Type Is A Boolean, Which Can Either Be True or False
alive = True
print("Are You Alive: " + str(alive))

alive = False
print("Are You Alive: " + str(alive))

print(type(alive))
