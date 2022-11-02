n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
a1=[]
for i in a:
    if i>=x and i<=y:
        a1.append(i)
if len(a1)>0:
    print(sum(a1))
else:
    print(-1)