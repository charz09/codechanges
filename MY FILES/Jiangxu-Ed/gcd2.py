def gcd(x,y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
GCD = gcd(x,y)
print("GCD is: ")
print(GCD)
