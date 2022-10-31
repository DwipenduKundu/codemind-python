n=int(input())
a=list(map(int,input().split()))
s,p=map(int,input().split())
sum=0
for i in a:
    if i not in range(s,p+1):
        sum+=i
print(sum)