n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    s=0
    while i!=0:
        t=i%10
        i//=10
        s+=1
    l.append(s)
sum=0
for i in l:
    if max(l)==i:
        sum+=1
print(sum)