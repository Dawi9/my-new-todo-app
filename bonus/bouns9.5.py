password = input("Enter your password: ")

lenght = len(password) >= 8
digit = any(char.isdigit() for char in password)
upper_case = any(char.isupper() for char in password)

if[(lenght), (digit), (upper_case)] == [True, True, True]:
    print("Your password is strong")
else:
    print("Your password is weak")










