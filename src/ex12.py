def vect(L: list[list[int]]) -> list[list[int]]:
    s: list[list[int]] = []
    f: list[list[int]] = [[0], [1]]
    n = len(L[0])

    while len(f) != 0:
        x = f.pop(0)

        if len(x) == n:
            s += [x]
        else:
            f += [x + [0]]
            f += [x + [1]]

    res: list[list[int]] = []

    for scal in s:
        vec: list[int] = []

        for j in range(len(s)):

