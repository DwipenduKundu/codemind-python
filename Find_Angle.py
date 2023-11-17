import math
a=int(input())
b=int(input())
d=math.degrees(math.atan(b/a))
if d-int(d)==0:
    print(int(d))
else:
    if abs(int(d)-d)>0.4:
        print(int(d)+1)
    else:
        print(int(d))