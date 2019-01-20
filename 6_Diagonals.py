# trial 1:\
# trial 2:/
# trial 3:

points=list()
trial = [1,2,3]
diag = list()
def check_points(point):
    if point not in points:
        return True
    return False

def add_diagnoal(diag, n):
    if len(diag) == n:
        print(diag)
        exit()

    for i in range(9):
        try_option(i)

def try_option(i):
    for k in trial:
        if k == 1:
            diag.append((i,k))
            point_b = i+1+int(i/3)
            point_c = i+4+int(i/3)
            if check_points(point_b) and check_points(point_c):
                points.append(point_b)
                points.append(point_c)
                break
            else:
                diag.pop()
        elif k == 2:
            diag.append((i,k))
            point_a = i+int(i/3)
            point_d = i+5+int(i/3)
            if check_points(point_a) and check_points(point_d):
                points.append(point_a)
                points.append(point_d)
                break
            else:
                diag.pop()
        elif k == 3:
            continue
add_diagnoal(diag = [], n=6)
print (points)
print (diag)
print (len(diag))
