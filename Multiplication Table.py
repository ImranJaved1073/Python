number = int(input("Enter number : ")) 

a = int(input("Repitition upto: ")) 
while a < 1:
    print("Enter a positive number.\n")
    a = int(input("Repitition upto:")) 

print("Table of" ,number,"is:\n")


for i in range(1,a+1):
    print( number, "  *  ", i, "  =   " , (number * i))
