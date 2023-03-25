# So We've Already Seen What Type Cast Can Do In The Variables.py
# But This Is A More Detailed Take On That Topic

# So In A Nutshell, We Have Functions That Can Be Used To Convert Data Types Into Different Ones
# This Can Be Useful For Example When You Are Trying To Concatenate (Combine) A String With A Number During Print

stringToWholeNumber = "5"

print(type(stringToWholeNumber))

stringToWholeNumber = int(stringToWholeNumber)
print(type(stringToWholeNumber))
print(stringToWholeNumber)

# Now That It Is A Number We Can Do Math Operations With It
print(stringToWholeNumber + 5)  # Which Would Results In 10

# If Were To Turn It Back Into A String It Would Give Us An Error Due To The Combination Of String And Number (Int)

# Because A Float Is Not A Whole Number So If We Were To Turn A Float Into An Integer
# It Would Cut The Decimals After The Point

floatyVariable = 7.5
wholeNumber = int(floatyVariable)

print(type(floatyVariable))
print(floatyVariable)

print(type(wholeNumber))
print(wholeNumber)

# A Boolean In General Is True Which Equals To 1 And False Which Equals To 0
# However There Are Plenty Of Languages Where 0 Is False And Everything Else Is True

boolean0 = bool(0)
boolean1 = bool(1)
boolean2 = bool(-2.1)

print("Boolean With Cast Value 0: " + str(boolean0))
print("Boolean With Cast Value 1: " + str(boolean1))
print("Boolean With Cast Value -2.1: " + str(boolean2))
