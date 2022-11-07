n=int(input())
a=list(map(int,input().split()))
s=s1=0
for i in range(n):
    if i%2==0:
        s+=a[i]
    elif i%2==1:
        s1+=a[i]
if abs(s-s1)==0:
    print("YES")
elif abs(s-s1)!=0:
    print("NO")