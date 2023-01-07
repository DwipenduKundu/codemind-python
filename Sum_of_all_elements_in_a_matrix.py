n,m=map(int,input().split())
m1=[]
c=0
for i in range(n):
    a=list(map(int,input().split()))
    m1.append(a)
    c+=sum(a)
print(c)