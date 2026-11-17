def combinaison_lineaires(c: int, V: list[int]) -> int:
    res = 0
    i = 0

    while i < len(V):
        res ^= V[i] * ((c >> i) & 1)
        i += 1

    return res

print(combinaison_lineaires(7,[2, 2, 11]))
print(combinaison_lineaires(7,[103, 21, 95]))
print(combinaison_lineaires(7,[188, 26, 89]))
print(combinaison_lineaires(12,[1, 12, 5, 14, 7, 3]))
print(combinaison_lineaires(10,[1, 26, 25, 18]))
print(combinaison_lineaires(6,[5, 21, 27, 16]))
print(combinaison_lineaires(8,[5, 1, 4, 11, 7]))
print(combinaison_lineaires(11,[2, 6, 2, 6, 4]))
print(combinaison_lineaires(29,[20, 62, 22, 4, 42, 58, 21]))
print(combinaison_lineaires(45,[5, 1, 5, 6, 5, 3, 7]))
