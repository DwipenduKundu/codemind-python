n=int(input())
rem=0
if n>=0:
    while n!=0:
        a=n%10
        n=n//10
        rem=(10*rem)+a
    print(rem)
elif n<0:
    while abs(n)!=0:
        a=abs(n)%10
        n=abs(n)//10
        rem=(10*rem)+a
    print(-rem)