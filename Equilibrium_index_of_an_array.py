a=int(input())
for _ in range(a):
    n=int(input())
    l=list(map(int,input().split()))
    flag=0
    for i in range(len(l)):
        if sum(l[:i])==sum(l[i+1:]):
            print(i)
            flag=1
            break
    if flag==0:
        print(-1)