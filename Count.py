a=int(input())
arr=[int(i) for i in input().split()]
count=sum=0
for i in range(len(arr)):
    if arr[i]%2==0:
        count+=1
    elif arr[i]%2!=0:
        sum+=1
print(count,sum)