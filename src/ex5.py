import math

def norme(V: list[float]) -> float:
    somme = 0

    for vi in V:
        somme += vi * vi

    return math.sqrt(somme)
