n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    if i>=0:
        l.append(len(str(i)))
    else:
        l.append(len(str(i))-1)
print(*l)