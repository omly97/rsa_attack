from factor.forcebrute import factorisation as fact_forcebrute
from factor.fermat import fermat as fact_fermat
from factor.factorielle import factorisation as fact_factorielle
from factor.rhopollard import fact_floyd


import sys
sys.setrecursionlimit(150000)


""" Test de factorisation """
items = [187, 5893, 7171, 3439, 799]

for n in items:
    print("\n\t --> Factorisation de ", n)

    # force brute
    facts = fact_forcebrute(n)
    print("methode force brute: {} = {} x {}".format(n, facts[0], facts[1]))

    # fermat
    facts = fact_fermat(n)
    print("methode Fermat: {} = {} x {}".format(n, facts[0], facts[1]))

    # factoriel
    facts = fact_factorielle(n)
    print("methode factorielle: {} = {} x {}".format(n, facts[0], facts[1]))

    # Pollard-Strassen

    # Rho-Pollard
    facts = fact_floyd(n)
    print("methode Rho-Pollard (Floyd): {} = {} x {}".format(n, facts[0], facts[1]))

