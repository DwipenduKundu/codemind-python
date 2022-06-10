n=int(input())
sum=0
prod=1
while n!=0:
    a=n%10
    n=n//10
    sum+=a
    prod*=a
print(prod-sum)