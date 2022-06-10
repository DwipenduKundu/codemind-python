n=int(input())
c=0
while n!=0:
    a=n%10
    n=n//10
    if a>c:
        c=a
print(c)