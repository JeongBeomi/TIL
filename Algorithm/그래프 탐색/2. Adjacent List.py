n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

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
# 1 2
# 0 3 4
# 0 4 5
# 1
# 1 2 6
# 2
# 4