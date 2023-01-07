n,m=map(int,input().split())
m1=[]
c=0
e=0
o=0
for i in range(n):
    a=list(map(int,input().split()))
    m1.append(a)
for i in range(n):
    for j in range(m):
        if m1[i][j]%2==0:
            e+=m1[i][j]
        else:
            o+=m1[i][j]
print(e,o)