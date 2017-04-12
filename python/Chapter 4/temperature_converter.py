print("Press C to convert from Fahrenheit to Celsius.")
print("Press F to convert from Celsius to Fahrenheit.")
choice = input("Your choice: ").upper()

if choice == "C":
    choice = "Celsius"
    convert_from = "Fahrenheit"
else:
    choice = "Fahrenheit"
    convert_from = "Celsius"

temp = int(input("Please enter the temperature in {}: ".format(convert_from)))

if choice == "Fahrenheit":
    temp = int((temp*(9/5) + 32))
else:
    temp = int((temp - 32) * (5/9))

print("The temperatue in {} is {}.".format(choice, str(temp)))
