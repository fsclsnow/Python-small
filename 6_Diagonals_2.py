# Option 0:/
# Option 1:\
# Option 2:
# points is a list of occupied points
# title is a list stored all options




def NoColide(ind, option):
    if option == 0:
        point_a = ind + int(ind/3)
        point_b = ind + 5 + int(ind/3)
        if point_a in points:
            return False
        if point_b in points:
            return False
        return True
    if option == 1:
        point_c = ind + 4 + int(ind/3)
        point_d = ind + 1 + int(ind/3)
        if point_c in points:
            return False
        if point_d in points:
            return False
        return True
    if option == 2:
        return True

def Add_diagonal(title, ind, n)
