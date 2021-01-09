
def cutting(n):
    ens = list(range(2, n))
    ens_cuttted = []
    index = 0
    length = 1

    while index < len(ens):
        ens_cuttted.append(ens[index:index + length])
        index += length
        length += 1

    return ens_cuttted

print(cutting(10))