def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
a=list(map(int,input().split()))
x=a.index(min(a))
y=a.index(max(a))
count=0
for i in range(len(a)):
    if is_prime(a[i])==True and x<=y and x<=i and y>=i:
        count+=1
    elif is_prime(a[i])==True and y<=y and y<=i and x>=i:
        count+=1
print(count)