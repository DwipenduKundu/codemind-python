n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    l.append(len(str(i)))
m=max(l)
f=[]
for i in range(len(a)):
    if len(str(a[i]))==m:
        f.append(a[i])
print(*f)