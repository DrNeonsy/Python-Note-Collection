# Let's Take At Strings A Bit Closer Starting With Basic Methods

txt = "This Is A String"

print("Length Of String: " + str(len(txt)))  # This Will Return The Length Of The String

print("The Letter Or String 's' Is Located At Index: " + str(txt.find("s")))
print("The Letter Or String 'S' Is Located At Index: " + str(txt.find("S")))
# This Will Return The Index Of The First Occurrence Of The String You Want To Find

# Important Note: This Will Return -1 If The String You Want To Find Does Not Exist
# Indexes: Always Starts At 0
# Also Like Most If Not All Things, This Is Case Sensitive

print(txt.capitalize())  # This Will Capitalize The First Letter Of The String

print(txt.upper())  # This Will Convert The Whole String To Upper Case

print(txt.lower())  # This Will Convert The Whole String To Lower Case

print(
    "Is This String A Number: " + str(txt.isdigit())
)  # This Will Check If The String Is A Number

print(
    "Only Characters In String: " + str(txt.isalpha())
)  # This Will Check If The String Is A Sequence Letter
# In This Case, It Will Return False Because We Also Have A "White"Space In There

print(
    "How Many 'i' In This String: " + str(txt.count("i"))
)  # This Will Count The Number Of Characters You Specify In The String

print(
    txt.replace("i", "x")
)  # This Will Replace The Characters You Specified With The Second "Parameter"

print(txt * 5)  # This Will Multiply The String With The Number You Specified
