n=int(input())
arr=list(map(int,input().split()))
o=[]
e=[]
f=[]
for i in arr:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
if len(e)>len(o):
    l=len(o)
else:
    l=len(e)
for i in range(l):
    f.append(o[i])
    f.append(e[i])
if len(e)>len(o):
    for i in range(len(o),len(e)):
        f.append(e[i])
elif len(e)<len(o):
    for i in range(len(e),len(o)):
        f.append(o[i])
if n%2!=0:
    f.append(0)
print(*f)