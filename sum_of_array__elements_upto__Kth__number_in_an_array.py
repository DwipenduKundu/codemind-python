n=int(input())
a=list(map(int,input().split()))
x=int(input())
sum=0
for i in range(x):
    sum+=a[i]
print(sum)