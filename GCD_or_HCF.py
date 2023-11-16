a,b=map(int,input().split())
while a!=0 and b!=0:
    if a>b:
        a%=b
    else:
        b%=a
if a!=0:
    print(a)
else:
    print(b)