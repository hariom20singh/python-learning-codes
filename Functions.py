def fabbonacci(i):
    if i<=0:
        return 0
    elif i==1:
        return 1
    else:
        return fabbonacci(i-1)+fabbonacci(i-2)
def getSum(a,b):
    return a+b
def printSum(a,b):
    print(a+b)
x = float(input())
y = float(input())

print(getSum(x,y))
printSum(x,y)
for i in range(6):
    print(fabbonacci(i))