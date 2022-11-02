def reverse(num):
    rev=0
    while num>0:
        r=num%10
        rev=rev*10+r
        num=num//10
    return rev
n=int(input())
a=list(map(int,input().split()))
count=0
for i in a:
    if i==reverse(i):
        count+=1
print(count)