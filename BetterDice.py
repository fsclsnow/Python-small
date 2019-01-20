
import itertools as it


def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

#count the number of each wins of the dices
    outcomelist = []
    for i in dice1:
        for j in dice2:
            outcomelist.append((i,j))
    for (i,j) in outcomelist:
        if i > j:
            dice1_wins += 1;
        elif j > i:
            dice2_wins += 1;

    if dice1_wins > dice2_wins:
        return True
    else:
        return False
#    print (dice1_wins, dice2_wins)
#dice1 = [1, 2, 3, 4, 5, 6]
#dice2 = [1, 2, 3, 4, 5, 6]
dice1 = [1, 1, 6, 6, 8, 8]
dice2 = [2, 2, 4, 4, 9, 9]

count_wins(dice1, dice2)

#Check if there is a dice win all other dices
def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    counts = dict()
    c = -1
    for i in dices:
        for j in dices:
            if j != i:
                if count_wins(i,j):
                    counts[dices.index(i)] = counts.get(dices.index(i),0) + 1
    for (i,j) in counts.items():
        if j == len(dices) - 1:
            c = i
    return c


dices1 = [[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]
dices2 = [[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]
dices3 = [[3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [4, 4, 4, 4, 0, 0], [5, 5, 5, 1, 1, 1]]

print (find_the_best_dice(dices1))
print (find_the_best_dice(dices2))
print (find_the_best_dice(dices3))
