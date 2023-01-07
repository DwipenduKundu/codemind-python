n,m=map(int,input().split())
m1=[]
c=[]
for i in range(n):
    a=list(map(int,input().split()))
    m1.append(a)
    c.append(sum(a))
print(max(c))