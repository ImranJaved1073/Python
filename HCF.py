number1 = int(input("Enter number 1: ")) 
while number1 < 0:
    print("ERROR! Number is invalid.\nEnter a number again.")
    number1 = int(input("Enter number 1: ")) 

number2 = int(input("Enter number 2: ")) 
while number2 < 0:
    print("ERROR! Number is invalid.\nEnter a number again.")
    number2 = int(input("Enter number 2: ")) 

i=0;   
for  i in range(1, number2+1):
   if number1 % i == 0 and number2 % i == 0: 
      hcf = i
        
print( "HCF of ",number1, " and ", number2," is:", hcf )
