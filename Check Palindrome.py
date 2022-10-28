sum = 0
rev = 0
print("ENTER A NUMBER FOR WHICH YOU WANTED TO PRINT REVERSE= ")
num = int(input())
x = num;
while x != 0:
	r = x % 10
	rev = rev * 10 + r
	x = x // 10
        
print("REVERSE IS:",rev)
if rev == num:
	print("Entered Number is a Palindrome.")
else:
	print("Entered Number is NOT Palindrome.")