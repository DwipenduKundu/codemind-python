n=int(input())
m=int(input())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
sum=0
for i in range(n):
    for j in range(m):
        sum+=a[i][j]
print(sum)