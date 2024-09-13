# Write a Python script that defines a list of strings representing various fruits l'apple', 'banana', 'orange', 'kiwi', 'pineapple', 'watermelon'], then implement a function to filter the words in the list that contain the substring 'apple' in a new filtered list. Print both the original list and the filtered list.
# The output will be as follows:
# Original list: ['apple', 'banana', 'orange', 'kiwi', 'pineapple', 'watermelon']
# Filtered List: ['apple', 'pineapple']

fruits = ['apple', 'banana', 'orange', 'kiwi', 'pineapple', 'watermelon']
filtered_fruits = []
for fruit in fruits:
    if 'apple' in fruit:
        filtered_fruits.append(fruit)
print(fruits)
print(filtered_fruits)