marks  = [99, 85, 72, 60, 45]

marks[1] = 88  # Update the second element
marks.append(95)  # Add a new mark at the end
marks.sort()  # Sort the marks in ascending order
print("Updated marks list:", marks)
print("Number of marks:", len(marks))  # Output: 6
print("Highest mark:", marks[-1])  # Output: 99
print("Third mark in the list:", marks[2])  # Output: 72

#slicing

print("First three marks:", marks[0:3])  # Output: [45, 60, 72]
print("Marks from index 2 to end:", marks[2:])  # Output: [72, 85, 88, 95, 99]
print("Last two marks:", marks[-2:])  # Output: [95, 99]

print(max(marks))  # Output: 99
print(min(marks))  # Output: 45

marks.clear()
print("Marks list after clearing:", marks)  # Output: []
