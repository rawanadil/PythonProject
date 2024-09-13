# Write a Python program that defines a function called
# 'check _num' which takes a single integer argument 'number' and returns if the number is even or odd. (Note: Check the numbers from 1 to 10).
# The output will be as follows:
# 1 is odd
# 2 is even
# 3 is odd
# 4 is even
# 5 is odd
# 6 is even
# 7 is odd
# 8 is even
# 9 is odd
# 10 is even

def num(y):
    if y % 2 == 0:
        return "even"
    else:
        return "odd"
for y in range(1, 11):
    e = num(y)
    print(f"{y} is: {e}")
