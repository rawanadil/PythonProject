# How does the program calculate the total cost based on area and price per meter?

i = float(input("Please enter length: \n"))
y = float(input("Please enter width: \n"))
r = float(input("How much for 1 meter? \n"))
e = str(i * y)
print("The total area is: " + e)
q = str(i * y * r)
print("Total cost: $" + q)
