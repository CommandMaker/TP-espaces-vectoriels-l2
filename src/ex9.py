def prod_scal(a: int, b: int) -> int:
    res = 0

    while a > 0 or b > 0:
        res ^= a & b
        a >>= 1
        b >>= 1

    return res & 1
