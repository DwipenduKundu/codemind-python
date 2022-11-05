import math
x=int(input())
y=list(map(int,input().split()))
a=[]
for i in range(len(y)):
    if((math.sqrt(y[i])-int(math.sqrt(y[i])))==0):
        a.append(y[i])
print(sum(a))