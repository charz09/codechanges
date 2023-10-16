def isprime(candidate):
    # No primes are even except 2.
    # ... Use modulo division to test for even numbers.
    if (candidate % 2) == 0:
        if candidate == 2:
            return True
        else:
            return False

    # Loop over numbers incrementing by 2 to the number.
    for i in range(3, candidate, 2):
        # No prime can be more than the square root.
        if (i * i) > candidate:
            break;
        # See if the number is evenly divisible.
        if (candidate % i) == 0:
            return False

    # The candidate is a prime unless it is 1.
    return candidate != 1


test=130
if isprime(test):
	print(test,"is a prime number")
else:
	print(test,"is not a prime number")

