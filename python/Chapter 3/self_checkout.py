item1 = int(input("Enter the price of item 1: "))
quantity1 = int(input("Enter the quantity of item 1: "))
item2 = int(input("Enter the price of item 2: "))
quantity2 = int(input("Enter the quantity of item 2: "))
item3 = int(input("Enter the price of item 3: "))
quantity3 = int(input("Enter the quantity of item 3: "))

total = float((item1*quantity1) + (item2*quantity2) +(item3*quantity3))
print("Subtotal: ${}".format(str(total)))
tax = 0.055 * total
print("Tax: ${}".format(str(tax)))
total += tax
print("Total: ${}".format(str(total)))

