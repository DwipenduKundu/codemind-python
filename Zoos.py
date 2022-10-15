s=input()
z=[]
o=[]
for i in range(len(s)):
    if s[i]=='z' or s[i]=='Z':
        z.append(s[i])
    elif s[i]=='o' or s[i]=='O':
        o.append(s[i])
if len(s)>20:
    print("No")
elif len(o)==2*len(z):
    print("Yes")
else:
    print("No")