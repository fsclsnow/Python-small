
diag_all=list()
diag=list()
import itertools as it

if len(diag) == 16:
    print (diag)
    exit()

for i in range(30):
    if i %6 != 0:
        diag_all.append((i,i+5))
    if i % 6 != 5:
        diag_all.append((i,i+7))

print (diag_all)
print (len(diag_all))

for i in range(36):
    diag.append()
