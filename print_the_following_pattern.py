a=int(input(""))
for i in range(a):
    for j in range(a):
        if((i==j)|(i==a-j-1)):
            print("x",end="")
        else:
            print("0",end="")
    print("")