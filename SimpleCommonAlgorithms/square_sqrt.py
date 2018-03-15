def calSqrt(Num):
    numTemp = Num
    count = 0
    factor = 1 # from 1 to the number of all sum factor
    while numTemp > 0:
        numTemp -= factor
        factor += 2
        count += 1
    if numTemp == 0:
        print(Num, 'is the square of', count)
    else:
        print(Num, 'is not a square number')

def square(base):
    squareNum = 0
    sumFactor = 1
    for i in range(0, base):
        squareNum += sumFactor
        sumFactor += 2
    print('The square of', base, 'is', squareNum)

# 361 = 19*19   362 is non-square 1521 = 39^2
# Test
calSqrt(361)
calSqrt(362)
calSqrt(1521)
square(19)