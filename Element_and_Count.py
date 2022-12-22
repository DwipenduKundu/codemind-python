n=int(input())
arr=list(map(int,input().split()))
a=[]
l=[]
for i in arr:
    if i not in l:
        a.append(arr.count(i))
        l.append(i)
for i in range(len(l)):
    print(l[i],a[i],end=' ')