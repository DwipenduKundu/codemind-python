n=int(input())
prod=1
sum=0
while n!=0:
    a=n%10
    n=n//10
    prod*=a
    sum+=a
if prod==sum:
    print("Spy Number")
else:
    print("Not Spy Number")