str=input().split()
c=0
for i in str:
    s=i.lower()
    if s==s[::-1]:
        c+=1
print(c)