def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
a=list(map(int,input().split()))
sum=count=0
for i in a:
    if is_prime(i)==True:
        sum+=i
        count+=1
print("%.2f"%(sum/count))