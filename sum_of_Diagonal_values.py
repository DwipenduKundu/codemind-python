n,m=map(int,input().split())
m1=[]
sum=0
for i in range(n):
    a=list(map(int,input().split()))
    m1.append(a)
for i in range(n):
    for j in range(m):
        if i==j:
            sum+=m1[i][j]
        if i==n-j-1 and i!=j:
            sum+=m1[i][j]
print(sum)