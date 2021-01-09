import math


def is_potential_squad(n):
    """ test si n (int) est un potentiel carre parfait """
    unite = n % 10
    dizaine =  ((n % 100) - unite) / 10

    if unite in [0, 1, 4, 5, 6, 9]:
        if unite == 0 and dizaine == 0:
            return True
        elif unite in [1, 4, 9] and dizaine % 2 == 0:
            return True
        if unite == 5 and dizaine == 2:
            return True
        elif unite == 6 and dizaine % 2 != 0:
            return True
        else:
            return False
    else:
        return False


def isquad(n):
    """ test si n (int) est un entier """
    if is_potential_squad(n):
        unite = n % 10
        i = 0

        while i + unite < math.sqrt(n):
            i += 10

        if i + unite == math.sqrt(n):
            return True
        else:
            return False
    else:
        return False


def fermat(n):
    """ factorisation de n par Fermat """
    a = int(math.sqrt(n)) + 1

    while not isquad((a*a - n) % n):
        a += 1
    b = int(math.sqrt((a*a - n) % n))

    return [a + b, max(a,b) - min(a, b)]

