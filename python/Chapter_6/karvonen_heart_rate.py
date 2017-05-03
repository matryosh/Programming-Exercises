input_num = False

while not input_num:
    try:
        resting_heart_rate = int(input("Resting pulse: "))
        age = int(input("Age: "))
        input_num = True
    except:
        print("Try to input an actual number this time.")

intensity = [i for i in range(55, 96, 5)]

target_rate = [int(float("{}".format((((220-age)-resting_heart_rate)\
                                       *(float("{0:.2f}".format(i/100))))+resting_heart_rate))) for i in intensity]

print("Intensity      | Rate   ")
print("------------------------")
for i in enumerate(intensity):
    print("{}%            | {}    ".format(intensity[i[0]], target_rate[i[0]]))
