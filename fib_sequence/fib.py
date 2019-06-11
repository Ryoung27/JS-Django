def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(20))


FibArray = [0,1]

def fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n<=len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
	FibArray.append(temp_fib)
	return temp_fib

print(fibonacci(500))
