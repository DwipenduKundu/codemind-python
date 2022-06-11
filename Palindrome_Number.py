x=int(input())
for i in range(x):
    n=int(input())
    temp=n
    rem=0
    while n!=0:
        a=n%10
        n=n//10
        rem=a+(rem*10)
    if rem==temp:
        print("True")
    else:
        print("False")