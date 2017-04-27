from math import log10

def calculate(balance, apr, payment):
    x = -0.33
    apr = apr/100
    w = 1-((1+(apr/365))**30)
    z = log10((1 + ((balance/payment)*w)))
    y = log10(1 + apr) 
    months = divmod(((x * (z//y)) * 365), 12)
    return int(months[0])

balance = int(input("What is your balance? "))
apr = int(input("What is the APR on the card (as a percent)? "))
payment = int(input("What is the monthly payment you can make? "))

print("It will take you {} months to pay off this card.".format(calculate(balance, apr, payment)))
