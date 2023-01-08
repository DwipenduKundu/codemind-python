n,m=map(int,input().split())
m1=[]
arr=[]
c=0
for i in range(n):
    a=list(map(int,input().split()))
    m1.append(a)
    l=a[:]
    l.sort()
    if l==a or l[::-1]==a:
        c+=1
print(c)
