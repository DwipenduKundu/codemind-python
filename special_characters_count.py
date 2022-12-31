str=input()
c=0
for i in str:
    if i.isalpha()==True:
        c+=1
    if i==' ':
        c+=1
print(len(str)-c)