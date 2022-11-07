n=int(input())
a=list(map(int,input().split()))
if len(a)>=3:
    l=max(a)
    for i in range(a.count(l)):
        a.remove(max(a))
    l=max(a)
    for i in range(a.count(l)):
        a.remove(max(a))
    print(max(a))
else:
    print(max(a))