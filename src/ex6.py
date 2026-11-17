def norme(V: list[float]) -> float:
    maxi = abs(V[0])

    for vi in V:
        if abs(vi) > maxi:
            maxi = abs(vi)

    return maxi
