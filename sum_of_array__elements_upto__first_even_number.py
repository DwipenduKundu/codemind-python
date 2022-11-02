n=int(input())
a=list(map(int,input().split()))
a1=[]
sum=0
for i in range(len(a)):
    if a[i]%2==0:
        l=i
        break
    else:
        l=len(a)
for i in range(l):
    sum+=a[i]
print(sum)