correct = False
years = 0

while not correct:
    try:
        rate = int(input("What is the rate of return? "))
        years = 72//rate
        correct = True
        print("It will take {} years to double your initial investment".format(years))
    except:
        print("Sorry. That's not a valid input.")
