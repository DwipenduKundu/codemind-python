s=input()
f=""
temp=""
for i in s:
    if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u") and temp!="V":
        f+="V"
        temp="V"
    else:
        if temp!="C":
            f+="C"
            temp="C"
print(f)