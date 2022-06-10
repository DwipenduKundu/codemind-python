a=int(input())
arr=[int(i) for i in input().split()]
for i  in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
for i in range(len(arr)):
    print(arr[i],end=" ")