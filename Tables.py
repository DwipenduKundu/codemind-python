x,y=input().split()
a,b=int(x),int(y)
for i in range(b+1):
    if i%2!=0:
        print(a,"x",i,"=",a*i)