# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

def find_root(v):
    for node in range(1, v + 1):
        if tree[node][2] == 0:
            return node

v = int(input())
tree = [[0] * 3 for _ in range(v + 1)]
edges = list(map(int, input().split()))

for i in range(0, len(edges), 2):
    parent, child = edges[i], edges[i + 1]
    if tree[parent][0] == 0:
        tree[parent][0] = child
    else:
        tree[parent][1] = child
    tree[child][2] = parent

root = find_root(v)

# 전위 순회
def pre_order(node):
    if node != 0:
        print(node, end=" ")
        pre_order(tree[node][0])
        pre_order(tree[node][1])

# 중위 순회
def in_order(node):
    if node != 0:
        in_order(tree[node][0])
        print(node, end=" ")
        in_order(tree[node][1])

# 후위 순회
def post_order(node):
    if node != 0:
        post_order(tree[node][0])
        post_order(tree[node][1])
        print(node, end=" ")

print('전위 순회 : ', end='')
pre_order(root)
print()

print('중위 순회 : ', end='')
in_order(root)
print()

print('후위 순회 : ', end='')
post_order(root)
print()

# 전위 순회 : 1 2 4 7 12 3 5 8 9 6 10 11 13 
# 중위 순회 : 12 7 4 2 1 8 5 9 3 10 6 13 11 
# 후위 순회 : 12 7 4 2 8 9 5 10 13 11 6 3 1