n,m=map(int,input().split())
m1=[]
sum=0
for i in range(n):
    a=list(map(int,input().split()))
    m1.append(a)
for i in range(n):
    for j in range(m):
        if i==0 or j==0 or j==n-1 or i==n-1:
            sum+=m1[i][j]
print(sum)