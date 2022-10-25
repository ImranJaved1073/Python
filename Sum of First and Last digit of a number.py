print("Find the first and last digit of a number:\n")
print("-----------------------------------------------\n")
x = int(input("Enter number: ")) 
first = x;
last = x % 10;

while first >= 10:
	first = first // 10

sum=first+last
print("The sum of first and last digit of entered number: ",sum)
