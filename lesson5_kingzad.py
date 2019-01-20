def dyangialPoints(index, position):
    if(position == 0):
        return -1,-1
    if(position == 1):
        a = index + (index // 6)
        d = index + 7 + (index//6)
        return a, d
    if(position == 2):
        b = index + 1 + (index//6)
        c = index + 6 + (index//6)
        return b, c

def noColision(p1, p2, collectionPoints):
    if(p1 == -1 and p2 == -1):
        return False
    if(p1 in collectionPoints):
        return False
    if(p2 in collectionPoints):
        return False
    return True

def printgrid(list):
    result = []
    for i in list:
        if i==0:
            result.append(' ')
        if i==1:
            result.append('\\')
        if i==2:
            result.append('/')
    print(result)


def NextMove(tiles, postion, collectionPoints):
    if(len(tiles)>= 25):
        i = 0
        for e in tiles:
            if(e > 0):
                i = i + 1
        if (i == 16):
            printgrid(tiles)
            #print(tiles)
        return
    
    ownTiles = tiles.copy()
    ownCollectionPoints = collectionPoints.copy()

    for position in [0,1,2]:
        ownTiles.append(position)
        p1, p2 = dyangialPoints(len(tiles), position)
        if(noColision(p1, p2, collectionPoints)):
            ownCollectionPoints.append(p1)
            ownCollectionPoints.append(p2)
        NextMove(ownTiles, position, ownCollectionPoints)


tile = []
collectionPoints = []
for i in [0,1,2]:
    NextMove(tile, i, collectionPoints)
