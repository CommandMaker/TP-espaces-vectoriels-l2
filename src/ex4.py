def combinaison_lineaire(c: list[int], V: list[list[int]], p: int) -> list[int]:
    res = [0] * len(V[0])
    i = 0

    while i < len(c):
        j = 0

        while j < len(V[i]):
            res[j] = (res[j] + V[i][j] * c[i]) % p
            j += 1

        i += 1

    return res


print(combinaison_lineaire([2, 2, 3], [[2, 3, 4, 1], [1, 1, 0, 2], [3, 2, 1, 1]], 5))
