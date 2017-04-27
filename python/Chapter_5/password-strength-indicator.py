import re

def password_validator(password):
    
    match_symbol = re.search(r'[!@#\$%\^&\*\?]', password)
    match_letter = re.search(r'[a-zA-Z]' , password)
    match_number = re.search(r'\d', password)
    if len(password) < 8:
        return 0

    if (match_letter and not match_symbol and not match_number) \
       or (match_number and not match_letter and not match_symbol):
        return 0
    elif match_number and match_letter and not match_symbol:
        return 1

    return 2

def return_password_strength(password,func):
    if func(password) == 0:
        print("The password {} is a very weak password.".format(password))
    elif func(password) == 1:
        print("The password {} is a strong password.".format(password))
    elif func(password) == 2:
        print("The password {} is a very strong password.".format(password))


return_password_strength('abcdef', password_validator)
return_password_strength('abc123xyz', password_validator)
return_password_strength('1337h@xor!', password_validator)

