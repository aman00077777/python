import time

count = int(input("Enter a number to start countdown: "))

print("Countdown starts now!!!")
for i in range(count, 0, -1):
    print(count)
    time. sleep(1)
    count -= 1


print("Whooooosh! Blast off! 🚀")