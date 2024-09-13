# How does this program classify the student's grade into letter grades?

r = float(input("Enter the student's grade: \n"))
if r >= 90:
    print("A")
elif r >= 75:
    print("B")
elif r >= 50:
    print("C")
else:
    print("F")