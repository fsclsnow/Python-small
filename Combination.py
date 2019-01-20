print ('This little program caluate combinations of n choose k')

while True:
    try:
        n = int(input('Please enter an integer as n:'))
    except:
        print ('Please enter a valid number')
    else:
        break

while True:
    try:
        k = int(input('Please enter an integer as k:'))
        if k > n:
            print ('k cannot larger than n')
            quit()
    except:
        print ('Please enter a valid number')
    else:
        break

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

print ('There are',(int((factorial(n)/((factorial(n-k))*(factorial(k)))))), 'combinations')
