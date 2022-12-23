n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    s=0
    while i!=0:
        t=i%10
        i//=10
        s+=t
    l.append(s)
print(sum(l))