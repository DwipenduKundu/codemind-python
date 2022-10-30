s=input()
c=0
for i in range(len(s)):
    if s[i].isnumeric()==True:
        c+=1
if c>0:
    print("Contains",c,"digit")
if c==0:
    print("Doesn't contain digit")