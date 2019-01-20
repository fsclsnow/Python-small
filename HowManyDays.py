print ('Given an daily interest rate, this tools will tell you how many days you need to reach a certain mount of money with the given deposit')
while True:
    try:
        deposit = float(input('Enter the initial DEPOSIT amount:'))
    except:
        print('Not a right number')
    else:
        break

while True:
    try:
        drate = float(input('Enter the daily interest rate:'))
    except:
        print('Not a right number')
    else:
        break

while True:
    try:
        target = float(input('Enter the target money amount:'))
    except:
        print('Not a right number')
    else:
        break

def DaytoReachTarget (deposit,drate,target):
    day = 1
    amount = deposit
    while amount < target:
        day = day + 1
        amount = amount * (1 + drate/100)
    print ('If you start with ', deposit, 'Dollars, you will reach', target, ' Dollars in', day, 'days')

DaytoReachTarget((deposit), (drate), (target))
