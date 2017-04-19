months = {
    1: "January",
    2: "Feburary",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
    }

month = int(input("Please enter the number of the month: "))

if month < 1 or month > 12:
    print("Not in range.")
else:
    print("The name of the month is {}".format(months[month]))
