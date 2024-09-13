#  How does this program handle age verification if the user confirms their nationality?

w = input("Are you Iraqi? Type yes or no: ").lower()
if w == "yes":
    print("You can.")
    yer = int(input("Enter your age: "))
    if yer >= 18:
        print("Okay")
    else:
        print("Can't")
else:
    print("No")