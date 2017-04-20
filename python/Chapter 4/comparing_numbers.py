first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

if first == second or first == third or second == third:
    exit
else:
    if first > second and first > third:
        print("The largest number is {}".format(first))
    elif first < second and second > third:
        print("The largest number is {}".format(second))
    elif first < third and second < third:
        print("The largest number is {}".format(third))
