n=int(input())
temp=b=n*n
sum=0
while b!=0:
    a=b%10
    b=b//10
    sum+=a
if n==sum:
    print("Neon Number")
else:
    print("Not Neon Number")