def test_prime(n):
    if (n==1):
        print(n,"is not a prime number")
        return False
    elif (n==2):
        print(n,"is a prime number")
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                print(n,"is not a prime number")
                return False
        print(n,"is a prime number")
        return True

print(test_prime(130))
