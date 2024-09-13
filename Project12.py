# Write a function to find the square of numbers from 1 to 5. The output will be as follows:
# The squared number of 1 is : 1
# The squared number of 2 is : 4
# The squared number of 3 is : 9
# The squared number of 4 is : 16
# The squared number of 5 is : 25?

r = 1
while r <= 5:
    t = r + 1
    g = r ** 2
    print(f"The squared num {t} is: {g}")
    r += 1