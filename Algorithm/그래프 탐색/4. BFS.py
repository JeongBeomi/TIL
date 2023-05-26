from collections import deque

def bfs(v):
    visited = [False] * (n + 1)
    q = deque([v])
    visited[v] = True
    print(v, end = " ")

    while q:
        v = q.popleft()
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                q.append(next_v)
                print(next_v, end = " ")

n, m = map(int, input().split())

edges = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for i in range(0, len(edges), 2):
    graph[edges[i]].append(edges[i + 1])
    graph[edges[i + 1]].append(edges[i])

bfs(1)
    
# [입력]
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

# [출력]
# 1 2 3 4 5 7 6