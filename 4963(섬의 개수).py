import sys

sys.setrecursionlimit(10000) 

def dfs(i,j):
    x = [1,-1,0,0,1,-1, 1,-1]
    y = [0,0,1,-1,-1,-1,1,1]

    for k in range(8):
        x_d = i + x[k]
        y_d = j + y[k]

        if island[x_d][y_d] == 1 and check[x_d][y_d] == 0:
            check[x_d][y_d] = 1
            dfs(x_d, y_d)

while True:
    island = []
    cnt = 0
    w,h = map(int, sys.stdin.readline().split())
    check = list([0]*(w+2) for _ in range(h+2))

    if w != 0:
        for _ in range(h):
            land = list(map(int, sys.stdin.readline().split()))
            land.insert(0, 0)
            land.insert(len(land), 0)
            island.append(land)
        island.insert(0, [0]*(w+2))
        island.insert(len(island), [0]*(w+2))

        for i in range(1,h+1):
                for j in range(1,w+1):
                    if island[i][j] == 1 and check[i][j] == 0:
                        check[i][j] = 1
                        dfs(i,j)
                        cnt += 1
        print(cnt)

    else:
        break

#통과