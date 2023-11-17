def maximumNumber(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if num_str[i] == '6':
            num_str = num_str[:i] + '9' + num_str[i+1:]
            break
    max_num = int(num_str)
    return max_num
num = int(input())
result = maximumNumber(num)
print(result)