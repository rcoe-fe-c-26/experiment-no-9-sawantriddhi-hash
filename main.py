# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder:Riddhi
# Date:30-01-2026

print("--- Factorial Finder ---\n")


# Write your code here 
N = int(input())

if N < 0:
    print(f"Factorial of {N} is Not Defined")
else:
    fact = 1
    for x in range(1, N + 1):
        fact = fact * x
    print(f"Factorial of {N} is {fact}")








