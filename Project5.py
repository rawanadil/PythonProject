 # How does the program handle unexpected responses?

w = input("Answer with yes, no, or maybe: \n").lower()
if w == "yes":
    print("Yes")
elif w == "no":
    print("No")
elif w == "maybe":
    print("Maybe")
else:
    print("Error")