a,b=map(int,input().split())
if a>=b:
    m=a
else:
    m=b
for i in range(m,1+(a*b)):
    if i%a==0 and i%b==0:
        print(i)
        break