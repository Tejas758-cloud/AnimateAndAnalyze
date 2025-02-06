import math

def is_prime(n):
    # Handle edge cases
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check divisibilty from 3 to the square root of n

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
        return True
    
    print(is_prime(73))
    print(is_prime(75))