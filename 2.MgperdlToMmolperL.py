x = float(input("Enter concentration in mg/dl: "))

molar_mass = float(input("Enter molar mass of molecule: "))

y = x / molar_mass * 10

print("Concentration in mmol/L is: ", y)