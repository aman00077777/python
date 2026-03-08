file = open("certificate.txt", "r")
data = file.read()
data = data.lower()

if "live" in data:
    print("Present")
else:
    print("Not Present")

    