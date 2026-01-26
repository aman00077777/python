food = ["pizza", "burger", "pasta", "salad", "sushi"]
print("Original list:", food)
food.append("ice cream")
print("After appending 'ice cream':", food)
food.remove("salad")
print("After removing 'salad':", food)
food.sort()
print("After sorting:", food)

print(len(food))  # Output: 5

print(food[2])  # Output: pasta

print(food[-1])  # Output: sushi