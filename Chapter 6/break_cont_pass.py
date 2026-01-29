# BREAK - exits the loop immediately
print("=== BREAK Example ===")
for i in range(5):
    if i == 3:
        break
    print(i)
# Output: 0, 1, 2

print("\n=== CONTINUE Example ===")
# CONTINUE - skips the current iteration and goes to the next one
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output: 0, 1, 3, 4

print("\n=== PASS Example ===")
# PASS - does nothing, placeholder for future code
for i in range(3):
    if i == 1:
        pass  # placeholder, could add code here later
    print(i)
# Output: 0, 1, 2

# PASS with function
def my_function():
    pass  # function body to be implemented later