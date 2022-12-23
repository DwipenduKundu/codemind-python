n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(0,n,2):
    temp=a[i+1]
    for j in range(temp):
        l.append(a[i])
print(*l)