import math
def is_prime(a):
    if a==1:
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return False
    return True
n=int(input())
l=[]
for i in range(2,n):
    if n%i==0 and is_prime(i)==True:
        l.append(i)
        n//=i
if len(l)==0:
    print(-1)
else:
    print(*l)