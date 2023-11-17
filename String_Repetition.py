s=input()
n=int(input())
c=s.count('a')
l=n//len(s)
r=n%len(s)
if r==0:
    print(c*l)
else:
    f=s[:r]
    c1=f.count('a')
    print((c*l)+c1)