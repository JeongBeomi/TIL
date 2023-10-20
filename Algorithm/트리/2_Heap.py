# 힙을 배열의 형태로 구현
# 왼쪽자식 인덱스 = 자신의 인덱스 * 2, 오른쪽 자식 = 자신의 인덱스 * 2 + 1
# 부모의 인덱스 = 자신의 인덱스 // 2

# 최소힙

# 힙 삽입 연산
def heap_push(item):
    heap.append(item)
    child = len(heap) - 1
    parent = child // 2

    while parent > 0 and heap[parent] > heap[child]:
        heap[parent] ,heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2

# 힙 삭제 연산
def heap_pop():
    # 힙이 루트노드 한개 일 때
    if len(heap) <= 2:
        return heap.pop()
    # 반환할 루트 노드 저장
    root = heap[1]
    # 리프노드를 루트노드로 이동
    heap[1] = heap.pop()
    parent = 1
    child = parent * 2
    # 자식노드가 존재하면 값 비교해서 더작을 경우 교환
    while child < len(heap):
        # 오른쪽 자식이 존재하고, 값이 더 작을 경우 child를 오른쪽 자식으로 변경
        if child + 1 < len(heap) and heap[child] > heap[child + 1]:
            child = child + 1
        # 자식이 더 작으면 노드 교환        
        if heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
            child = parent * 2
        # 최소힙 만족하면 탈출
        else:
            break
            # 백업한 루트노드 반환
    return root

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