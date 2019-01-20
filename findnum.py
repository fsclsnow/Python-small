#find a 6 digits number starts with 100 and can be divied by 9127
x=100000
num=list()
while x < 101000:
    num.append(x)
    x = x+1
for i in num:
    if i % 9127 == 0:
        print (i)
    else:
        continue
