# A For Loop Is Yet Another "Head Controlled" Loop So Just Like The While Loop
# Because It's "Head Controlled" (The Conditions Comes Before The Code Block)

# The Difference? A While Loop Repeats "While" The Condition Is True (Unknown Number Of Times)
# A For Loop Repeats "For" A (Specific) Number Of Times (Known Number Of Times)

for i in range(10):
    print("Execution 0-9: ", i)
    # You Can Put An Else To The End Which Executes When The Condition | Code Execution Is Done
else:
    # THis Won't Be Executed If You Hit A "Break" Keyword (Check Break Section)
    print("Loop Is Done")

# We Can Also Loop Through Collections Like A String

for i in "Hello World":
    print(i)
