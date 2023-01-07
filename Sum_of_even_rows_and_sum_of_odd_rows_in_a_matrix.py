n,m=map(int,input().split())
m1=[]
c=0
e=0
o=0
for i in range(n):
    a=list(map(int,input().split()))
    m1.append(a)
    if (i+1)%2==0:
        e+=sum(a)
    else:
        o+=sum(a)
print(o,e)