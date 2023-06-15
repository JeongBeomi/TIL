numbers = [1, 2, 3, 4]
n = len(numbers)

# 1_재귀조합
def combination(arr, start):
    if len(arr) == combination_length:
        print(arr)
        return
    
    for i in range(start, n):
        arr.append(numbers[i])

        combination(arr, i + 1)

        arr.pop()

combination_length = 3
combination([], 0)

# 2_비트연산자
for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            print(numbers[j], end = " ")
    print()
        

# 3_라이브러리

from itertools import combinations

for line in combinations(numbers, 3):
    print(line)