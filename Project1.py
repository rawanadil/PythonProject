#  How does this program convert seconds into hours, minutes, and seconds
# hours, minutes, and seconds?
t = int(input("Please enter time in seconds: \n"))
h = t // 3600
m = (t % 3600) // 60
s = t % 60
print(f"This duration is: {h} hours, {m} minutes, and {s} seconds")