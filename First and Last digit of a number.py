print("Find the first and last digit of a number:\n")
print("-----------------------------------------------\n")
x = int(input("Enter number: ")) 
first = x;
last = x % 10;

while first >= 10:
	first = first // 10

print("The first digit of entered number: ",first)
print("The last digit of entered number: ",last)
