
num=14

def isPerfectSquare(num):
    i=1
    while num>0:
        num-=i
        i+=2
    return num==0
print(isPerfectSquare(num))
print(isPerfectSquare(16))