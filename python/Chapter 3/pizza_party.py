people = int(input("How many people? "))
pies = int(input("How many pizzas do you have? "))
slices_per_pie = int(input("How many slices are in each pie? "))

total_slices = pies * slices_per_pie

total = total_slices // people
leftover = total_slices % people

print("{} people with {} pizzas".format(str(people), str(pies)))
print("Each person get {} pieces of pizza.".format(str(total)))
print("There are {} leftover pieces".format(str(leftover)))
