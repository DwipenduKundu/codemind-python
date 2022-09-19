x=int(input())
temp=s=x**2
temp2=x
st=str(s)
l=len(st)
l2=len(str(x))
arr,arr2=[],[]
for i in range(l):
    arr.append(temp%10)
    temp=temp//10
for i in range(l2):
    arr2.append(temp2%10)
    temp2=temp2//10
f=0
for i in range(l2):
    if arr[i]==arr2[i]:
        f=1
    else:
        f=0
        break
if f==1:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")