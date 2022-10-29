n=int(input())
m=int(input())
x=n+m
np=x+1
while True:
    is_prime=True
    for i in range(2,int(np**0.5)+1):
        if np%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(np-x)
        break;
    np+=1