from datetime import date

year = date.today().year
current_age = int(input("What is your current age? "))
retired_age = int(input("At what age would you like to retire? "))
years_to_retirement = retired_age - current_age
year_to_retire = year + years_to_retirement

year = str(year)
years_to_retirement = str(years_to_retirement)
year_to_retire = str(year_to_retire)

print("You have {} years left until you can retire.".format(years_to_retirement))
print("It's {}, so you can retire in {}".format(year, year_to_retire))

