# 반복문
def selection_sort1(arr):
    for i in range(len(arr) - 1):
        min_index = i

        for j in range(i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

# 재귀
def selection_sort2(idx):
    if idx == len(numbers) - 1:
        return
    
    min_idx = idx

    for j in range(idx, len(numbers)):
        if numbers[min_idx] > numbers[j]:
            min_idx = j
    
    numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]
    selection_sort2(idx + 1)


numbers = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]
# selection_sort1(numbers)
selection_sort2(0)
print(numbers)