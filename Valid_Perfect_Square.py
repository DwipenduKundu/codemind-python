import math
n=int(input())
for i in range(n):
    a=int(input())
    if((math.sqrt(a)-int(math.sqrt(a)))==0):
        print("True")
    else:
        print("False")