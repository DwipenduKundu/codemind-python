n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    l=x+y
    l.sort()
    print(*l)