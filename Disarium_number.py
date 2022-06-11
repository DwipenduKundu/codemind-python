n=int(input())
count=0
temp=n
while n!=0:
    a=n%10
    n=n//10
    count+=1
n=temp
sum=0
while n!=0:
    a=n%10
    n=n//10
    sum=(a**count)+sum
    count-=1
if sum==temp:
    print("True")
else:
    print("False")