import math
from factor.mymath import isprime


def list_prime_number(n):
    return [n for n in range(2, int(math.sqrt(n)) + 1) if isprime(n)]


def forcebrute(n):
    factor = 1
    for x in list_prime_number(n):
        if n % x == 0:
            factor = x
            break
    return factor


def factorisation(n):
    d = forcebrute(n)
    return [d, n // d]
