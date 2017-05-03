total = 0

for i in range(5):
    try:
        num = int(input("Enter a number: "))
    except:
        num = 0
    finally:
        total += num

print("The total is {}.".format(total))
