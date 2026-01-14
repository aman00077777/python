str = input("Enter a string: ")
mid= len(str) // 2
output1 = str[mid -1 : mid +2]
print("Middle three characters:", output1)
output2 = str[-2 : ]
print("Last two characters:", output2)