principal = float(input("Enter the principal: "))
roi = float(input("Enter the rate of interest: "))
years = float(input("Enter number of years: "))

simple_interest = principal*(1+((roi/100)*years))

print("After {} years at {}%, the investment will be worth ${:.2f}.".format(years, roi, int(simple_interest)))
