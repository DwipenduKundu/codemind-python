a=int(input())
for i in range(a):
    x,y=(input().split())
    count=0
    for j in range(int(x),int(y)+1):
        if j%10==2 or j%10==3 or j%10==9:
            count+=1
    print(count)