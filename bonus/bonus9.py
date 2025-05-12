from unicodedata import digit

password = input("Enter your password: ")

result={}


if len(password) >= 8:
    result["Lenght"] = True
else:
    result["Lenght"] = False


digit = False
for i in password:
    if i.isdigit():
        digit = True


result["digits"] = digit

uppercase = False
for i in password:
        if i.isupper():
            uppercase = True


result["upper-case"] = uppercase

print(result)
if all(result.values()):
    print("Your password is strong")
else:
    print("Your password is weak")

