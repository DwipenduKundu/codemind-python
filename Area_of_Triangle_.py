import math
x, y ,z= input().split()
s=(int(x)+int(y)+int(z))/2
print("%0.2f"%math.sqrt(s*(s-int(x))*(s-int(y))*(s-int(z))))