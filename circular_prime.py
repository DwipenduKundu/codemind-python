x=int(input())
is_prime=True
for i in range(2,int(x**0.5)+1):
    if x%i==0:
        is_prime=False
        break

if is_prime==True:
    xrev=int((str(x)[::-1]))
    ip=True
    for i in range(2,int(xrev**0.5)+1):
        if xrev%i==0:
            ip=False
            break
    if ip==True:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")