def build_Vect(relation: list[float]) -> list[list[float]]:
    res: list[list[float]] = []
    i = 0

    while i < len(relation) - 1:
        r: list[float] = [0] * len(relation)
        r[0] = -relation[i + 1] / relation[0]
        r[i+1] = 1

        res += [r]
        i += 1

    return res


print(build_Vect([1, 1, 1]))
print(build_Vect([2, -3, 5]))
