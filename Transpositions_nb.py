# This little program find the transpositions which makes "MARINE" to "AIRMEN"
# which we can only swtich positions of neighbour letters
word = 'MARINE'
target = 'AIRMEN'
airmen=list()

seq=list(word)
seqt=list(target)
sequ=list()

def sequence():

    for a in range(6):
        while seq[a] != seqt[a]:
            n = seq.index(seqt[a])
            p1 = seq[n-1]
            p2 = seq[n]
            seq[n-1]=(p2)
            seq[n]=(p1)
            sequ.append((n-1,n))
        continue
    print (sequ)
    return sequ

sequence()
