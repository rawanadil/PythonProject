# What conditions must be met for the user to be able to drive according to this program?

u = int(input("Enter your age: \n"))
t = input("Do you have a license (yes or no)? \n")
if u >= 18 and t.lower() == "yes":
    print("You can.")
else:
    print("You can't.")