import math
def calculate_gcd(numbers):
    gcd = numbers[0]
    for num in numbers[1:]:
        gcd = math.gcd(gcd, num)
    return gcd
n=int(input())
numbers = list(map(int, input().split()))
result = calculate_gcd(numbers)
print(result)