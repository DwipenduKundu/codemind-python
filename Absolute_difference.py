import math
def is_pri(a):
    if a==1:
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
p=[]
np=[]
for i in l:
    if is_pri(i)==True:
       p.append(i)
    elif is_pri(i)==False:
       np.append(i)
pp=1
pnp=1
for i in p:
    pp*=i
for i in np:
    pnp*=i
print(abs(pnp-pp))