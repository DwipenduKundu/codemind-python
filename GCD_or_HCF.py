# Extended Euclid's algorithm to find out GCD of two given number
a,b=map(int,input().split())
while a!=0 and b!=0:
    if a>b:
        a%=b
    elif b>a:
        b%=a
if a==0:
    print(b)
else:
    print(a)