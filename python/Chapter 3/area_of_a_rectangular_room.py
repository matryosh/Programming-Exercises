length = int(input("What is the length of the room in feet? "))
width = int(input("What is the width of the room in feet? "))
area = length * width
feet_to_meters = str((area) * 0.09290304)
length = str(length)
width = str(width)
area = str(area)

print("You entered dimensions of {} feet by {} feet.".format(length, width))
print("The area is\n{} square feet\n{} square meters".format(area, feet_to_meters))
