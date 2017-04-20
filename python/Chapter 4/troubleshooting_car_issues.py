car = input("Is the car silent when you turn the key? ")

if car.lower() == "y":
    car = input("Are the battery terminals corroded? ")

    if car.lower() == "y":
        print("Clean terminals and try starting again.")
    else:
        print("Replace cables and try again.")
else:
    car = input("Are the battery terminals corroded? ")
    if car.lower() == "y":
        pass
    else:
        car = input("Are the battery terminals corroded? ")
        if car.lower() == "y":
            pass
        else:
            car = input("Are the battery terminals corroded? ")
            if car.lower() == "y":
                car = input("Are the battery terminals corroded? ")
                if car.lower() == "y":
                    pass
                else
            else:
                print("Can't help. Sorry")
