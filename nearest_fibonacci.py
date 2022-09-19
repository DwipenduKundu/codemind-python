a,b=0,1
x=int(input())
for i in range(x):
    c=a+b
    t=b
    b=a+b
    a=t
    if abs(x-b)<=abs(x-a):
        f=b
    if abs(x-b)==abs(x-a):
        f=b
        l=a
if abs(x-f)!=abs(x-l):
    print(f)
else:
    print(l,f)