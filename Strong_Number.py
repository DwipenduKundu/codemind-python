n=int(input())
temp=n
prod=1
sum=0
while n!=0:
    prod=1
    a=n%10
    n=n//10
    for i in range(1,a+1):
        prod*=i
    sum+=prod
if temp==sum:
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")