import re

def validate_first_name(first_name):
    if len(first_name) >= 2 and not re.search(r'\d', first_name):
        return True

def validate_last_name(last_name):
    if len(last_name) >= 2 and not re.search(r'\d', last_name):
        return True

    return False

def validate_employee_id(employee_id):
    if re.search(r'[A-Z][A-Z]-\d+', employee_id) and len(employee_id) == 7:
        return True

    return False

def validate_zip(zipcode):
    if re.search(r'\D', zipcode):
        return False

    return True

def validate_input(first_name, last_name, employee_id, zipcode):

    valid_first = validate_first_name(first_name)
    valid_last = validate_last_name(last_name)
    valid_id = validate_employee_id(employee_id)
    valid_zip = validate_zip(zipcode)
    errors = list()
    
    if valid_first and valid_last and valid_id and valid_zip:
        print("There were no errors found")
    else:
        if not valid_first:
            errors.append("{} is not a valid name. It is too short.".format(first_name))
        if not valid_last:
            errors.append("{} is not a valid name. It is too short.".format(last_name))
        if not valid_id:
            errors.append("{} is not a valid ID.".format(employee_id))
        if not valid_zip:
            errors.append("The ZIP code must be numeric.")
    

    for i, j in enumerate(errors):
        print(j)


first = input("Enter the first name: ")
last = input("Enter the last name: ")
zipcode = input("Enter the ZIP code: ")
employee_id = input("Enter an employee ID: ")

validate_input(first, last, employee_id, zipcode)
    
