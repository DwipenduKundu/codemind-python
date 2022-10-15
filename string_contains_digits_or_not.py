n=int(input())
for i in range(n):
    s=input()
    flag=0
    for j in range(len(s)):
        if s[j].isdecimal()==True:
            flag=1
            break
        else:
            flag=0
    if flag==1:
        print("Yes")
    if flag==0:
        print("No")