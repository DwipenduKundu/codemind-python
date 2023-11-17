n=int(input())
while n!=1 and n!=7 and n!=4:
    a=list(map(int,str(n).strip()))
    c=0
    for i in a:
        c+=i**2
    n=c
if n==1 or n==7:
    print(True)
elif n==4:
    print(False)