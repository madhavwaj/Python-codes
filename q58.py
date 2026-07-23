#58. Write a python program to remove all the duplicates from a list
numbers = [1, 3, 5, 3, 7, 1, 9, 5]
unique_numbers = []

# Loop through each element
for target in numbers:
    # Add to new list only if it's not already there
    if target not in unique_numbers:
        unique_numbers.append(target)

print("List after removing duplicates (loop):", unique_numbers)
