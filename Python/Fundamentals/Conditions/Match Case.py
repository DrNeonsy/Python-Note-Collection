# Another More Precise Statement Is The Match Case (Also Known As Switch Case In Most Languages)

# Here You Use A Variable And Match Against It So In This Case We Perform Action Based On The Case That Is True

# Because We Define Cases, You Cannot Perform A Range Condition Like An If Statement

number = int(input("Enter A Number Between 0 - 10: "))

match number:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case 5:
        print("five")
    case _:
        print("unknown")
