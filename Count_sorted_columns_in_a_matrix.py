n,m=map(int,input().split())
m1=[]
arr=[]
c=0
for i in range(n):
    a=list(map(int,input().split()))
    m1.append(a)
for i in range(m):
    l=[]
    for j in range(n):
        l.append(m1[j][i])
    s=l[:]
    s.sort()
    if s==l or s[::-1]==l:
        c+=1
print(c)