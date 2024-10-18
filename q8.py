from sympy import *
N=19
if N==0:
    print("No computational required")
elif N>0:
    for i in range(1,N+1):
        if  isprime(i):
            print(i,end=" ")
else:
    n=abs(N)
    for j in range(1,n+1):
            print(2*j,end=" ")        
