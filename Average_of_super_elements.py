n=int(input())
a=list(map(int,input().split()))
vis = []
a1=[]
l=False
for i in a:
    if a.count(i) == i and i not in vis:
        a1.append(i)
        l=True
    vis.append(i)
if l==True:
    print("%.2f"%(sum(a1)/len(a1)))
if l==False:
    print(-1)