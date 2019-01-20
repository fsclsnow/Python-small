# trial 1:\
# trial 2:/
# trial 3:
# piont_a is LB; point_b is RB; point_c is LU; point_d is RU
# Not Finished
print ('Program not finished')
quit()

points=list()
diag = list()
i=0
def check_points(point):
    if point not in points:
        return True
    return False

def add_diagonal(diag, n):
    if len(diag) == n:
        print(diag)
        exit()
    try_option(i)

def try_option(i):
    if i == 25:
        len(diag) < 16
        try_option(i-1,k+1)
    else:
        point_b = i+1+int(i/5)
        point_c = i+6+int(i/5)
        point_a = i+int(i/5)
        point_d = i+7+int(i/5)
        if k == 1:
            diag.append((i,k))
            if check_points(point_b) and check_points(point_c):
                points.append(point_b)
                points.append(point_c)
            else:
                diag.pop()
        elif k == 2:
            if (i,(k-1)) in diag:
                points.remove(point_b)
                points.remove(point_c)
                diag.remove((i,(k-1)))
                diag.append((i,k))
                if check_points(point_a) and check_points(point_d):
                    points.append(point_a)
                    points.append(point_d)
                else:
                    diag.pop()
            else:
                diag.append((i,k))
                if check_points(point_a) and check_points(point_d):
                    points.append(point_a)
                    points.append(point_d)
                else:
                    diag.pop()
        elif k == 3:
            if (i,(k-2)) in diag:
                points.remove(point_b)
                points.remove(point_c)
                diag.remove((i,(k-2)))
            if (i,(k-1)) in diag:
                points.remove(point_a)
                points.remove(point_d)
                diag.remove((i,(k-1)))
        try_option(i+1)

add_diagonal(diag = [], n=16)
print (len(diag))
