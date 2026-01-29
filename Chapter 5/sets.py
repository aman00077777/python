food = {"pizza", "burger", "pasta", "salad", "pizza", "burger"}
print(food)
print(type(food))

food.add("sushi")
print(food)
food.remove("pasta")
print(food)
food.discard("steak")  # Does not raise an error if the item is not found
print(food)
