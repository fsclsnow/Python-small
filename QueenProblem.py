# find possible solutions that n queens put in a n*n chess
# board and they don't attack each other.
# .combination(p,r)  组合 r-length tuples, in sorted order, no repeat element
# .permutations(p.r) 排列 r-length tuples, all possible order, no repeat element


import itertools as it

def is_solution (perm):
    for (i1,i2) in it.combinations(range(len(perm)), 2):
        if abs(i1-i2) == abs(perm[i1]-perm[i2]):
            return False
    return True


while True:
    N = input('Enter Number of Chess Lines:')
    num = list()
    if len(N) < 1: break
    try:
        int(N)
    except:
        print('Not a number')
        continue

    if int(N) > 10:
        print ('Please choose a smaller number, otherwise it will take too much time')

    else:
        for perm in it.permutations(range(int(N))):
            if is_solution(perm):
                print(perm)
                num.append(perm)
    print (len(num))
