n=int(input())
a=list(map(int,input().split()))
b=int(input())
t=0
for i in range(n):
    if a[i]==b:
        print(i,end=' ')
        t=1
if t==0:
    print(-1)