n=int(input())
a=list(map(int,input().split()))
b=int(input())
a.sort()
t=c=0
for i in range(len(a)):
    if b==a[i]:
        print(i,end=' ')
        t=1
        c+=1
if c==1:
    print(a.index(b))
if t==0:
    print(-1,-1)