# This little program find the transpositions which makes "MARINE" to "AIRMEN"
word = 'MARINE'
target = 'AIRMEN'

seq=list(word)
seqt=list(target)
sequ=list()

def sequence():

    for a in range(6):
        if seq[a] == seqt[a]:
            continue
        else:
            n = word.find(seqt[a])
            p1 = seq[a]
            p2 = seq[n]
            seq[a]=(p2)
            seq[n]=(p1)
            sequ.append((a,n))
    print (sequ)
    return sequ

sequence()
