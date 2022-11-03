n=int(input())
a=list(map(int,input().split()))
b=int(input())
vis = []
a1=[]
l=False
for i in a:
    if a.count(i) == b and i not in vis:
        print(i,end=' ')
        l=True
    vis.append(i)
if l==False:
    print(-1)