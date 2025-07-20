option_No = 3

match option_No:
    case 1:
        print("Selected option 1")
    case 2:
        print("Selected option 2")
    case _:
        print("Please select an option between 1 - 2")


day = 7

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Day is a weekday")
    case 6 | 7:
        print("Weekends")
        

fruits = ["apple","banana","mangoos"]
for x in fruits:
    print(x)
    if x == "banana":
        break

for x in range(3):
    print(x)


