from collections import deque

def dfs(v):
    # 방문 리스트
    visited = [False] * (len(graph) + 1)
    # 스택
    s = deque([v])
    visited[v] = True

    while s:
        v = s.pop()
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                s.append(next_v)

graph = [
		[1, 2],
		[0, 3, 4],
		[0, 4, 5],
		[1],
		[1, 2, 6],
		[2],
		[4]
]

dfs(0)  # 0번 정점에서 시작
