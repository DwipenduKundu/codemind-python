n=int(input())
for i in range(n):
    n=int(input())
    a=list(map(int,input().split()))
    s=((n*(n+1))//2)-sum(a)
    print(s)