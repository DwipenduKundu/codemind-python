n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(n):
    if len(str(a[i]))%2==0:
        sum+=1
print(sum)