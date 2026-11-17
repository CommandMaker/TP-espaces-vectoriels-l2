def est_combinaison_linéaire(x: list[float], c: list[float], V: list[list[float]]) -> bool:
    i = 0
    process = True

    while i < len(x) and process:
        j = 0
        res = 0

        while j < len(c):
            res += V[j][i] * c[j]
            j += 1

        process = res == x[i]
        i += 1

    return process


print(est_combinaison_linéaire([9, 2, 6, 3, 9, 1],[-2, -3, -5, 2, -3],[[5, 1, 9, 9, 7, 4], [8, 8, 9, 7, 1, 3], [6, 6, 8, 3, 3, 9], [5, 9, 2, 2, 8, 4], [7, 4, 4, 5, 3, 3]]))
print(est_combinaison_linéaire([-24, 2, -22],[2, 2, 0, -5, -3],[[5, 8, 8], [4, 1, 9], [8, 5, 8], [6, 2, 7], [4, 2, 7]]))
