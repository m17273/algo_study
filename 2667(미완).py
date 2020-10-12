import sys

num = int(sys.stdin.readline())

graph = []
visited = []




for _ in range(num):
    graph.append(list(str(sys.stdin.readline().rstrip())))

for _ in range(num):
    visited.append(list(str(0)*num))
