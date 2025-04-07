import math


def isPrime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False

    # Check divisibility from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    # If no divisors were found, n is prime
    return True


if __name__ == "__main__":
    n = 11
    if (isPrime(n)):
        print("true")
    else:
        print("false")
