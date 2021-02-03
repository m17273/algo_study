import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
nodes = {1:[]}
checker = [0]* (N+1)
visited = [0] * (N+1)
visited[1] = 1

for _ in range(N-1):
    a,b = map(int, sys.stdin.readline().split())
    if a in nodes:
        nodes[a].append(b)
        if b in nodes:
            nodes[b].append(a)
        else:
            nodes[b] = [a]
    else:
        nodes[a] = [b]
        if b in nodes:
            nodes[b].append(a)
        else:
            nodes[b] = [a]

def dfs(target):
    visited[target] = 1
    for i in range(len(nodes[target])):
        next = nodes[target][i]
        if visited[next] != 1:
            checker[next] = target
            dfs(next)

for j in range(len(nodes[1])):
    checker[nodes[1][j]] = 1
    dfs(nodes[1][j])

for k in checker[2:]:
    print(k)

#통과