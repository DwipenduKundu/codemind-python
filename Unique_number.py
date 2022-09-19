x=input()
l=len(x)
arr=[]
temp=int(x)
for i in range(l):
    arr.append(temp%10)
    temp=temp//10
arr1=set(arr)
if len(arr)==len(arr1):
    print("Unique Number")
else:
    print("Not Unique Number")