weight = float(input("Enter your weight: "))
unit = input("(L)bs or (K)gs: ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not valid")

