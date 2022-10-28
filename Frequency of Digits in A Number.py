print("Find frequency of each digit in a given integer:")
print("-----------------------------------------------------")
print("Input any number:")
number = int(input())

for digit in range(0, 10):
    count = 0
    apparentNumber = number
    while apparentNumber > 0: 
        lastDigit = apparentNumber % 10;
        if (lastDigit == digit):
            count=count+1
        apparentNumber //= 10
    print("The frequency of",digit,"=",count)        