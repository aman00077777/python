import os 

file = open("new.txt","r")
data = file.read()
print(data)
file.close()    

os.rename("newsss.txt","Aman.txt")
os.remove("out.txt")