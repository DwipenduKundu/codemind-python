s=input()
c=0
for i in range(len(s)):
    if s[i].isnumeric()==True:
        c+=int(s[i])
print(c)