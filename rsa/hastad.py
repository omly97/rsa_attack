

def euclide_etendu(a, b):
    if b == 0:
        return [a, 1, 0]
    else:
        res = euclide_etendu(b, a % b)
        return [res[0], res[2], res[1] - (a // b) * res[2]]


def hastad(e1, c1, e2, c2, n):
    euclide = euclide_etendu(e1, e2)
    print(euclide)
    if euclide[0] == 1:
        return (pow(c1, euclide[1])* pow(c2, euclide[2])) % n
    else:
        return "cles inorrectes"

#print(hastad(7, 11, 11, 143, 187))
print(euclide_etendu(4543322112211, 787654321187))