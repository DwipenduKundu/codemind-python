n=int(input())
a=list(map(int,input().split()))
m=[]
for i in range(len(a)):
    mul=1
    for j in range(i):
        mul*=a[j]
    for j in range(i+1,len(a)):
        mul*=a[j]
    m.append(mul)
for i in m:
    print(i,end=' ')