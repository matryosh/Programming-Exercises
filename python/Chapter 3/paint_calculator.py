from math import ceil
one_gallon_350_feet = 350
width = int(input("How wide is the room? "))
length = int(input("What is the room's length? "))
area = length * width
amount_of_paint = (area)/one_gallon_350_feet

print("You will need to purchase {} gallons of paint to cover {} square feet.".\
      format(str(ceil(amount_of_paint)), str(area)))
