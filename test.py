from itertools import combinations_with_replacement
for c in combinations_with_replacement("TBLE", 7):
    print("".join(c))
