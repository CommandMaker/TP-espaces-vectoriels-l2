def prod_scal(V: list[int], W: list[int], p: int) -> int:
    res = 0
    i = 0

    while i < len(V):
        res += V[i] * W[i]
        i += 1

    return res % p
