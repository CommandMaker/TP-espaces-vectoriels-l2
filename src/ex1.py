def combinaison_lineaire(c: list[float], V: list[list[float]]) -> list[float]:
    res: list[float] = [0] * len(V[0])
    i = 0

    while i < len(c):
        j = 0

        while j < len(V[i]):
            res[j] += V[i][j] * c[i]
            j += 1

        i += 1

    return res
