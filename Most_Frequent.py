n=int(input())
a=list(map(int,input().split()))
g=0
f=a[0]
for i in a:
    if a.count(i)>g:
        g=a.count(i)
        f=i
    elif a.count(i)==g:
        if f>i:
            f=i
print(f)