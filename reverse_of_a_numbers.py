n=int(input())
rem=0
if n>=0:
    while n!=0:
        a=n%10
        n=n//10
        rem=(10*rem)+a
    print(rem)