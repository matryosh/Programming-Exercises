weight = int(input("Your weight in pounds: "))
height = int(input("Your height in inches: "))

bmi = (weight / (height * height)) * 703
print("Your BMI is {:05.2f}".format(bmi))

if bmi > 18.5 and bmi < 25:
    print("You are within the ideal weight range.")
elif bmi <= 18.5:
    print("You are underweight. You should see a doctor.")
elif bmi >= 25:
    print("You are overweight. You should see a doctor.")
