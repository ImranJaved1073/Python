x = int(input("Enter number: ")) 

count = 0

while x != 0:
    x = x // 10
    count += 1

print("Number of digits=",count)
