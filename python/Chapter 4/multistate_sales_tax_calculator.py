order = float(input("What is the order amount? "))
state = input("What state do you live in? ")
tax = 0.0

if state == "Wisconsin":
    county = input("What county? ")
    tax = 0.050

    if county == "Eau Claire":
        tax += 0.005
    elif county == "Dunn":
        tax += 0.004
elif state == "Illinois":
    tax += 0.080

if tax == 0.0:
    print("The total is ${}.".format(order))
else:
    print("The tax is {:04.2f}.\nThe total is ${:04.2f}.".format(tax, (order+(tax*order))))
    
