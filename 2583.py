import sys

M,N,K = map(int, sys.stdin.readline().split())
box = [[0]*N for _ in range(M)]
answer = []
s = []

for _ in range(K):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    for j in range(y1,y2):
        for k in range(x1, x2):
            box[j][k] = 1

for a in range(M):
    for b in range(N):
        if box[a][b] == 0:
            s.append((a,b))
            box[a][b] = 1
            cnt = 1

            while s:
                dx = [1,-1,0,0]
                dy = [0,0, 1, -1]

                t_x, t_y = s.pop()

                for i in range(4):
                    x = t_x+dx[i]
                    y = t_y+dy[i]

                    if 0 <= x < M and 0 <= y < N and box[x][y] == 0:
                        s.append((x,y))
                        box[x][y] = 1
                        cnt += 1
            answer.append(cnt)
answer.sort()
print(len(answer))
for i in answer:
    print(i, end=' ')

#통과