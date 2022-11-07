n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    sum=0
    for j in range(n):
        if a[i]>a[j]:
            sum+=1
    print(sum,end=' ')