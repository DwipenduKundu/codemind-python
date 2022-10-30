s=input()
v=0
c=0
d=0
sp=0
for i in range(len(s)):
    if s[i]==" ":
        sp+=1
    if s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U" or s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
        v+=1
    if s[i].isnumeric()==True:
        d+=1
print("Vowels:",v)
print("Consonants:",len(s)-v-d-sp)
print("Digits:",d)
print("White spaces:",sp)