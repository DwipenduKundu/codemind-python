s=input()
sum=0
for i in range(len(s)):
    if s[i].isdigit()==True:
        sum+=int(s[i])
print(sum)