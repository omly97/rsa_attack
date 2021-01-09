import math
from factor.mymath import gcd


def pollard(n):
    """ rho Pollard : methode iterative """
    f = lambda x: (x*x + 1) % n
    x = 2
    dic = dict([])

    while f(x) not in dic.values():
        dic[x] = f(x)
        x = dic[x]

    x2 = 0
    for key,val in dic.items():
        if val == f(x):
            x2 = key
            break

    gcd1 = gcd(abs(x - x2), n)
    if n % gcd1 == 0:
        return gcd1
    else:
        return gcd(abs(x + x2), n)


def floyd(n):
    """ rho Pollard : methode de Floyd """
    f = lambda x: x*x + 1
    torue = int(math.sqrt(n))
    lievre = torue
    d = 1

    while d == 1:
        torue = f(torue)
        lievre = f(f(lievre))
        d = gcd(abs(lievre - torue), n)

    return d


def fact_rhopollard(n):
    d = pollard(n)
    return [d, n // d]


def fact_floyd(n):
    d = floyd(n)
    return [d, n // d]
