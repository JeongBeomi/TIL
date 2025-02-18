# 분할정복과 재귀를 활용한 정렬 알고리즘 기법
def merge(left_arr, right_arr):
    merge_arr = []
    i, j = 0, 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            merge_arr.append(left_arr[i])
            i += 1
        else:
            merge_arr.append(right_arr[j])
            j += 1

    merge_arr += left_arr[i:]
    merge_arr += right_arr[j:]
    return merge_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])

    return merge(left_arr, right_arr)

numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)