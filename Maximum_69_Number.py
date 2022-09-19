num=input()
l=len(num)
arr=[]
temp=int(num)
for i in range(l):
    arr.append(temp%10)
    temp=temp//10
for i in range(l):
    if arr[l-i-1]==6:
        arr[l-i-1]=9
        break
for i in range(l):
    print(arr[l-i-1],end="")