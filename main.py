# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder:Riddhi
# Date:30-01-2026

print("--- Factorial Finder ---\n")


# Write your code here
print("---Factorial Finder----\n")  
N = int(input("Enter Number:"))
fact = 1
for N in range(N , 0 , -1):
    fact = fact*N
if(N<0):
    print(f"Factorial of {abs(N)} is Not Defined")
else:
    print(f"Factorial of {N} is {fact}")    



