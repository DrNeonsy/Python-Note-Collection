# Slicing Is An Extraction Of Elements From Some Sort Of "Collection" And A String Is A Collection Of Characters
# So In This Case "String Slicing" Allows Us To Extract A Part Of It "Substring"

# With Slicing There Are Three Arguments You Can Use (Where To Start, Where To Stop, How Far To Go)

text = "Hello World"

# Remember That Indexes Are "Zero Based" They Start From 0 For The First "Instance"
print(text[0:5])

# You May Assume That You Need "4" To Reach The "o" But The First Argument Is Inclusive And The Second Exclusive

# You Can Also Use text[:5] For The Same Result Because Python Will Assume That You Start From 0

print(text[:5])

# The Same Goes For The Last Index Position So You Can Either Do This

print(text[6:11])

# Or

print(text[6:])

# The Third Argument Defines The Steps Which By Default Are 1
# So If We Set It To 2 Then We Will Get Every 2 "Instance" Or In This Case Every 2 Character

print(text[::4])

# You Can Also Reverse A String By Using "text[::-1]"

print(text[::-1])

# Because It's Called Slicing We Should Probably Take A Look At The slice() Function
# It Works Almost Identical, However You Have To Use A "," Comma

# While A Collection Of "Elements" Or "Instances" Has A Positive Index It Can Also Have A Negative One
# The Only Difference Here Is The The "Normal" One Starts From Left And The Negative One From The Right Side

# You Are Not Using The slice() Function Directly Which Can Be A Bit Confusing
# It Is Used To Create "A Slice Object" Which Is Just Used To Define The Slicing Range Within A Variable

# A Good Example Is A String That Starts And Ends The Same Where You Would Only Want To Keep The Middle

web1 = "https://www.google.com"
web2 = "https://www.bing.com"
web3 = "https://www.microsoft.com"

# So The Domain Starts At Index 12 And Ends At 4 From The Right Side
slicing = slice(12, -4)

print(web1[slicing])
print(web2[slicing])
print(web3[slicing])
