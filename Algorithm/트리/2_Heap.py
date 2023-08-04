# 힙을 배열의 형태로 구현
# 왼쪽자식 인덱스 = 자신의 인덱스 * 2, 오른쪽 자식 = 자신의 인덱스 * 2 + 1
# 부모의 인덱스 = 자신의 인덱스 // 2

# 최소힙

# 힙 삽입 연산
def heap_push(item):
    heap.append(item)
    child = len(heap) - 1
    
    pass

# 힙 삭제 연산
def heap_pop():
    pass

heap = [0]
heap_push(2)
heap_push(5)
heap_push(7)
heap_push(3)
heap_push(4)
heap_push(6)
print(heap)

while len(heap) >= 2:
    print(heap_pop())