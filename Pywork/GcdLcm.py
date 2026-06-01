def gcd(a,b):
    i=min(a,b)
    while i>0:
        if a%i==0 and b%i==0:
            return i
        i-=1    
    if i==0:
        return 1

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("GCD of", a, "and", b, "is:", gcd(a,b))
print("LCM of", a, "and", b, "is:", (a*b)//gcd(a,b))