# This Section Is Going To Teach You How To Receive Input From A User
# For This We Have A Built-In Function input()

# var = input(); | This Would Prompt The User To Enter A String Without A Message
# Every Input That Is Not Casted Will Be A String By Default

txt = input("Enter A String: ")
integer = int(input("Enter An Integer: "))
floatValue = float(input("Enter A Float: "))

print("String Input: " + txt)
print("Integer Input: " + str(integer))
print("Float Input: " + str(floatValue))

# So That's User Input In Python: You Use The Input() Function And Situational Cast It Otherwise It'll Be A String
