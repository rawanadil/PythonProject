#  How does the program respond to a city that is not on the list?

city = input("Choose a city: Cairo, Alexandria\n")
if city.lower() == "cairo":
    print("You chose Cairo")
elif city.lower() == "alexandria":
    print("You chose Alexandria")
else:
    print(f"Sorry, {city} is not on our list")