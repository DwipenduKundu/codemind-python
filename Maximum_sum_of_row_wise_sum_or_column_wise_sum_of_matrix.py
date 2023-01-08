n,m=map(int,input().split())
m1=[]
c=0
arr=[]
for i in range(n):
    a=list(map(int,input().split()))
    m1.append(a)
    c+=sum(a)
    arr.append(sum(a))
for i in range(m):
    sum=0
    for j in range(n):
        sum+=m1[j][i]
    arr.append(sum)
print(max(arr))