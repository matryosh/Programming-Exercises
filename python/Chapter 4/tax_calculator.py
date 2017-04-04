amount = float(input("What is the order amount? "))
state = input("What is the state? ")
tax = 0.55

if state.upper() == "WI":
    print("The subtotal is ${:.2f}.".format(amount))
    print("The tax is ${}.".format(tax))
    amount = amount + tax

print("The total is ${:.2f}".format(amount))
    
