weight = int(input("What is your weight? "))
gender = input("What is your gender? ")
drinks = int(input("How many drinks have you had? "))
time = int(input("Hours since last drink? "))

r = 0.73 if gender == "male" else 0.66

BAC = ((drinks*5.14)/(weight*r)) - (0.015*time)
BAC = float("%.2f" % BAC)

print(BAC)

if BAC >= 0.08:
    print("It is not legal for you to drive.")
else:
    print("You can drive.")
