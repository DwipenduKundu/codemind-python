n=int(input())
a=list(map(int,input().split()))
s,p=map(int,input().split())
l=0
for i in a:
    if i not in range(s,p+1):
        print(i,end=' ')
        l=1
if l==0:
    print(-1)