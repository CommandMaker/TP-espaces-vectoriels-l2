def list_vecteurs(n: int) -> list[list[int]]:
    res: list[list[int]] = []
    i = 0

    while i < (1 << n):
        j = 0
        r: list[int] = []

        while j < n:
            r = [(i >> j) & 1] + r
            j += 1

        res += [r]
        i += 1

    return res


print(list_vecteurs(3))
