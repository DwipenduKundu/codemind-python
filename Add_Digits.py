n=int(input())
sum=0
while n!=0:
    a=n%10
    n=n//10
    sum=sum+a
    if((sum>=10)and(n==0)):
        n=sum
        sum=0
print(sum)