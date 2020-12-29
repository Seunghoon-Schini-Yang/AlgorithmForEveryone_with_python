## Recursion

# Fibonacci Recursion
def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibo(n-1)+fibo(n-2)
print(fibo(10))

# Factorial Recursion
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
print(fact(5))

# Euclid GCD Recursion
def GCD(a,b):
    if b==0:
        return a
    return GCD(b,a%b)
print(GCD(60,35))

# Tower of Hanoi Recursion
def hanoi(n):
    if n==1:
        return 1
    return 2*hanoi(n-1)+1
print(hanoi(4))