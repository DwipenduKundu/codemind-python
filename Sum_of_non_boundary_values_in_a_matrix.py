n,m=map(int,input().split())
m1=[]
s=0
for i in range(n):
    a=list(map(int,input().split()))
    m1.append(a)
for i in range(n):
    for j in range(m):
        if i!=0 and j!=0 and j!=m-1 and i!=n-1:
            s+=m1[i][j]
print(s)