x=int(input())
np=x+1
while True:
    is_prime=True
    for i in range(2,int(np**0.5)+1):
        if np%i==0:
            is_prime=False
            break
    if is_prime==True:
        l1=np
        break;
    np+=1
np=x
while True:
    is_prime=True
    for i in range(2,int(np**0.5)+1):
        if np%i==0:
            is_prime=False
            break
    if is_prime==True:
        l2=np
        break;
    np-=1
if abs(x-l1)>abs(x-l2):
    print(abs(x-l2))
else:
    print(abs(x-l1))