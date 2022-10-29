n,m=map(int,input().split())
nr=int(str(n)[::-1])
l1=len(str(n))
print(abs(int(str(n)[:m])-int(str(n)[l1-m:l1])))