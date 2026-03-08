file = open("report.txt","a")
file.write("\n I am from Bihar")
file.close()

file = open("report.txt","r")
data = file.read()
print(data)
file.close()