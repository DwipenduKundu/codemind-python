n,m=map(int,input().split())
a=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
g=a[0][0]
for i in range(n):
    g=a[0][0]
    for j in range(m):
        if a[j][i]>g:
            g=a[j][i]
    print(g)