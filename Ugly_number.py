def isUgly(n):
    if n > 0:
        factors = [2, 3, 5]
        for i in factors:
            while n % i == 0:
                n = n // i
        return n == 1
    else:
        return 0
n=int(input())
if isUgly(n)==True:
    print("Ugly Number")
else:
    print("Not Ugly Number")