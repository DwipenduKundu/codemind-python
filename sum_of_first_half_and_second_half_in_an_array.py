n=int(input())
a=list(map(int,input().split()))
a1=[]
sum1=0
sum2=0
for i in range(n//2):
    sum1+=a[i]
for i in range(n//2,n):
    sum2+=a[i]
print(sum1)
print(sum2)