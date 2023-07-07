import sys
sys.stdin = open('input.txt')

def check(num):
    if parent[num] != num:
        parent[num] = check(parent[num])
    return parent[num]

V, E = map(int, sys.stdin.readline().split())
parent = [0 for _ in range(V+1)]
node = []
result = 0

for _ in range(E):
    a, b, p = map(int, sys.stdin.readline().split())
    node.append([p, a, b])

node.sort()

for z in range(E):
    x = check(node[z][1])
    y = check(node[z][2])
    print(f'node={node}, z={z}')
    print(f'x={x}, y={y}')
    print(f'parent={parent}')
    if x < y:
        x, y = y, x
    if x and y and x != y:
        parent[x] = y
        result += node[z][0]
    elif not x and not y:
        parent[x] = y
        result += node[z][0]

print(result)
