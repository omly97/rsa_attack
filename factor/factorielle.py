from factor.mymath import gcd, factorial


def factorial_modulo(k, n):
    return factorial(k) % n


def factor(n):
    if factorial_modulo(n-1, n) == n - 1:
        return 1
    else:
        k = 1
        while gcd(factorial_modulo(k, n), n) <= 1:
            k += 1
        return k


def factorisation(n):
    d = factor(n)
    return [d, n // d]
