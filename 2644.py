import sys
from collections import deque

n = int(sys.stdin.readline())
target1, target2 = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())

familymap = [[0]*n for _ in range(n)]
checker = [0]*n

def dfs(start):
    tmp = deque([start])

    while tmp:
        a = tmp.popleft()

        for i in range(n):
            if familymap[a][i] == 1 and checker[i] == 0:
                checker[i] = checker[a] + 1
                tmp.append(i)

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    familymap[x-1][y-1] = familymap[y-1][x-1] = 1

dfs(target1-1)

if checker[target2-1] != 0:
    print(checker[target2-1])
else:
    print(-1)

#체크용 리스트를 2차원으로 만드는 것 보다 1차원에서 간단하게 해결할 수 있도록 짜기!
#이전 노드의 값을 계속해서 누적해가는 방식 생각해보기