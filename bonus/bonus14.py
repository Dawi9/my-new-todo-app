feet_inches = input("Enter feet and inches: ")


def parse(feetinches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

f, i = parse(feet_inches)
print("Fi", f, i)
result = convert(f, i)

if result < 1:
    print("This kid is too young to slide.")
else:
    print("This kid is allowed to slide.")