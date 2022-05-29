x,y,z=input().split()
count=0
for i in range(int(x),int(y)+1):
    if(i%int(z)==0):
        count+=1
print(count)