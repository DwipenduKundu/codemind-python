n=int(input())
a=list(map(int,input().split()))
s,p=map(int,input().split())
ar=[]
l=0
for i in a:
    if i not in range(s,p+1):
        ar.append(i)
        l=1
if l==1:
    print(max(ar))
if l==0:
    print(-1)