def norme(V: list[float]) -> float:
    somme = 0

    for vi in V:
        somme += abs(vi)

    return somme
