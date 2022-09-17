a=int(input())
b=int(input())
for i in range(a,b+1):
    temp=i
    f=0
    while temp!=0:
        n=temp%10
        temp=temp//10
        if n==0:
            f=0
            break
        elif i%n==0:
            f=1
        else:
            f=0
            break
    if f==1:
        print(i,end=' ')