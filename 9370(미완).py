import sys

T = int(sys.stdin.readline())
n, m, t = map(int, sys.stdin.readline().split())
s, g, h = map(int, sys.stdin.readline().split())

graph = []
x_what = []
d_box = []

for _ in range(n):
    graph.append(['INF']*n)
   
for i in range(m):
    a, b, d = map(int, sys.stdin.readline().split())
    graph[i][i] = 0
    graph[a-1][b-1] = d
    graph[b-1][a-1] = d
    d_box.append(d)

d_box.sort()

for _ in range(t):
    x = int(sys.stdin.readline())
    x_what.append(x)

for j in d_box:
    for i in range(n):
    
        if graph[s-1][i] == j:
            for num in range(n):
                if graph[i][num] != 0 and graph[i][num] != 'INF':
                    if graph[s-1][i] > graph[i][num] + graph[s-1][i]:
                        graph[s-1][i] == graph[i][num] + graph[s-1][i]


