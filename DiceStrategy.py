
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

#Find the strategy to win the game.
def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0
    if find_the_best_dice(dices) != -1:
        strategy["choose_first"] = True
        strategy["first_dice"] = find_the_best_dice(dices)
    else:
        strategy["choose_first"] = False
        strategy["first_dice"] = "False"
        for i in dices:
            for j in dices:
                if j != i:
                    if count_wins(i,j) == False:
                        strategy[dices.index(i)] = dices.index(j)
    return strategy

dices1 = [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]
dices2 = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]
print (compute_strategy(dices1))
print (compute_strategy(dices2))
