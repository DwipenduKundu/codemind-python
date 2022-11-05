a=int(input())
y=[int(i) for i in input().split()]
r=[]
vis=[]
for i in y:
    if y.count(i)>1 and i not in vis:
        r.append(i)
    vis.append(i)
print(r[0])