n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
vis=[]
for i in a:
    if i in b and i not in vis:
        print(i,end=' ')
    vis.append(i)