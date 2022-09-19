x=int(input())
f=0
for i in range(x//2):
    if i*(i+1)==x:
        f=1
        break
    else:
        f=0
if f==1:
    print("YES")
else:
    print("NO")