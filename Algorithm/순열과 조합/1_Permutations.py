# 1_재귀 순열
def permutation(arr):

    if len(arr) == permutation_length:
        print(arr)
        return
    
    for i in range(len(numbers)):
        if not visted[i]:
            arr.append(numbers[i])
            visted[i] = True

            permutation(arr)

            arr.pop()
            visted[i] = False

numbers = [1, 2, 3, 4]
visted = [False] * len(numbers)
permutation_length = 2  # 원하는 순열의 원소 개수

permutation([])

# 2_라이브러리사용

from itertools import permutations

for line in permutations(numbers, permutation_length):
    print(line)