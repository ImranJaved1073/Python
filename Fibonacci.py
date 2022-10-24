def fib(n):
    if n <= 0:
        print("Incorrect input")
    elif n== 1:
        return 0
    elif n== 2:
        return 1
    else:
        return fib (n- 1) + fib (n- 2)
 
num = int(input("Enter a term number: "))  
print("The",num,"term of fibonacci sequence is",fib(num))
