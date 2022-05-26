a=int(input())
b=int(input())
rev=0
for i in range(a,b+1):
    rev=0
    temp=i
    while i!=0:
        b=i%10
        rev=(rev*10)+b
        i=i//10
    if temp==rev:
        print(temp,end=" ")