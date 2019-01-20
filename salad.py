# This little program print out all possible options of choosing 7 ingredents from 4 materials (Tomato, Bell pepper, Lectuce and Eggplant)

from itertools import combinations_with_replacement
for c in combinations_with_replacement("TBLE", 7):
    print("".join(c))
