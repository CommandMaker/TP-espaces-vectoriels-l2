def liste_vecteurs(p: int, n: int) -> list[list[int]]:
    res: list[list[int]] = []

    for i in range(p**n): # pyright: ignore[reportAny] To prevent basedpyright from saying anything about p**n
        vec: list[int] = []
        j = 0
        while j < n:
            vec = [i % p] + vec
            i //= p
            j += 1

        res += [vec]


    return res


print(liste_vecteurs(3, 3))
