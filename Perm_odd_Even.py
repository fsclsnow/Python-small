# This little program check if a permutation is an even one or odd one

#def is_permutation(p):
#      return (set(p)==set(range(len(p))))

#print (is_permutation([0]))
#print (is_permutation([0,2,1]))
#print (is_permutation([1,2,3]))

def is_even_perm(p):
    stdp = range(len(p))
    i=0
    for a in range(len(p)):
        while p[a] != stdp[a]:
            n = p.index(stdp[a])
            p1 = p[n-1]
            p2 = p[n]
            p[n-1]=(p2)
            p[n]=(p1)
            i = 1 - i
    return (i == 0)

print (is_even_perm([0,3,2,4,5,6,7,1,9,8]))
#print (is_even_perm([3,1,2,0,4]))
print (is_even_perm([0,1,2,3,4,5,6,7,8,9,10,11,12,14,13,15]))
