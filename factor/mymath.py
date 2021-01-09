import math


def isprime(n):
    """ test de primalite par la méthode naïve: d <= sqrt(n) """
    if n == 1:
        return False
    else:
        response = True
        d = 2
        while d < int(math.sqrt(n)):
            if n % d == 0:
                response =  False
                break
            else:
                d += 1
        return response


def gcd(a, b):
    """ Calcul de PGCD: pgcd(a, b) = pgcd(b, a mod b) avec a > b """
    a = abs(a)
    b = abs(b)
    if min(a, b) == 0:
        return max(a, b)
    else:
        return gcd(min(a, b), max(a, b) % min(a, b))


def factorial(n):
    """ calcul factoriel par recursivire """
    n = abs(n)
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
