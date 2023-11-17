import math

def calculate_lcm(numbers):
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = lcm * num // math.gcd(lcm, num)
    return lcm
n=int(input())
numbers = list(map(int, input().split()))
result = calculate_lcm(numbers)
print(result)