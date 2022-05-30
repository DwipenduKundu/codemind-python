a=int(input())
y=[int(i) for i in input().split()]
r=[]
for i in y:
    if i not in r:
        r.append(i)
for i in range(len(r)):
    print(r[i],end=" ")