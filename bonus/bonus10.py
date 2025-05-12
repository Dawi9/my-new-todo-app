try:
    width = float(input("Enter the width of the rectangle: "))
    length = float(input("Enter the length of the rectangle: "))
    if width == length:
        exit("That look like a square. Please enter a different value for width and length.")


    area = width * length
    print(f"The area of the rectangle is {area} square units.")
except ValueError:
    print("Invalid input. Please enter numeric values.")
