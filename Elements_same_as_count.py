n=int(input())
a=list(map(int,input().split()))
vis = []
l=False
for i in a:
    if a.count(i) == i and i not in vis:
        print(i,end=' ')
        l=True
    vis.append(i)
if l==False:
    print(-1)