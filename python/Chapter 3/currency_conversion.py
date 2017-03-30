euros=float(input("How many euros are you exchanging? "))
rate=float(input("What is the exchange rate? "))

amount = (euros * rate)/100

print("{} euros at an exchange rate of {} is {:.2f} U.S. dollars.".format(str(int(euros)), str(rate), amount))
