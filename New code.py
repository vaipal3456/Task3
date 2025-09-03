n=int(input("Enter a number "))
def factorial(n):
    if n<2:
        return 1
    else:
        return n * (factorial(n-1))
result = factorial(n)
print(f"factorial of 5 is: {result}")

n=int(input("Enter a number "))
from math import *
print(f" Square root: {sqrt(n)}")
print(f" Logarithm: {log(n,2.5)}")
print(f" sine: {sin(n)}")

