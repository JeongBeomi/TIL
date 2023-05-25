n, m = map(int, input().split())  # 정점, 간선
graph = [[0] * n for _ in range(n)]

# 인접 행렬 생성
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

# 인접 행렬 출력
for i in graph:
    print(*i)

# 입력
# 7 7
# 0 1
# 0 2
# 1 3
# 1 4
# 2 4
# 2 5
# 4 6

# 출력
# 0 1 1 0 0 0 0
# 1 0 0 1 1 0 0
# 1 0 0 0 1 1 0
# 0 1 0 0 0 0 0
# 0 1 1 0 0 0 1
# 0 0 1 0 0 0 0
# 0 0 0 0 1 0 0