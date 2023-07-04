sample_list = [55, 7, 78, 12, 42]
# sample_list = [("철수", 55), ("영희", 7), ("민수", 78), ("기영", 12), ("유라", 42)] # key에 따른 정렬

def bubble_sort(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
            # if a[j][1] > a[j + 1][1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

print(bubble_sort(sample_list))  

# 출력
# [7, 12, 42, 55, 78]