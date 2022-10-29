n=int(input())
temp=n
t=f=0
for i in range(1,n+1):
    if n%i==0:
        f+=1
if f==2:
    t=1
if t==1:
    l=0
    while temp!=0:
        a=temp%10
        temp//=10
        if a==2 or a==3 or a==5 or a==7:
            l=1
        else:
            l=0
            break
    if l==1:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")