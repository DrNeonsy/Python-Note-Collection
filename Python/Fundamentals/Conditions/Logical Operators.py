# Logical Operators Are Deeply Tied With If Statements Or Any Conditional Expression

# We Have The "and" (Which Is Usually &&) And The "or" (Which Is Usually ||) And The "not" (Which Is Usually !=)

# But In Python We Write The Words

# So The Not Equals Operator Can Be Used The "Usual Way" Or The Python Way Which Is The Word "not"
# So If You Write "not" You Will Have To Do It At The Beginning Of A Condition That Is Inside Round Braces ()

if not (5 == 4):
    print("5 Is Not Equal To 4")

# The and Or & Needs All Linked Conditions To Be True To Return True
# So If One Of The Asked Conditions Bound By & Are False Then The Entire Thing Is False

if 5 == 6 and 6 == 6:
    print("This Is Not True")
else:
    print("5 Is Less Than 6 And 6 Is Equal To 6")

# The or Works Similar To The And However As The Word Suggests The Or Only Needs One True Condition

if 10 == 6 or 6 == 6:
    print("Same As Before Using The or Keyword")
