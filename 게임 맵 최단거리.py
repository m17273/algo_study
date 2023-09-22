# 통과
# checker에 이동한 경로를 표시하므로, queue에 좌표값이 있는지 없는지 확인할 필요 없음(주석처리 부분)

from collections import deque

def solution(maps):

    n = len(maps) # x좌표
    m = len(maps[0]) # y좌표
    checker = []

    for _ in range(n):
        checker.append([0] * m)

    answer = bfs(maps, checker, n, m)
    return answer

    
def bfs(maps, checker, n, m):
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque([[0,0]])
    checker[0][0] = 1

    while queue:
        
        num1 = queue[0][0]
        num2 = queue[0][1]

        queue.popleft()

        for i in range(4):
            x = num1 + dx[i]
            y = num2 + dy[i]

            if x < 0 or y < 0 or x >= n or y >= m:
                continue

            elif maps[x][y] == 1 and checker[x][y] == 0: #and [x,y] not in queue
                queue.append([x,y])
                checker[x][y] = checker[num1][num2] + 1

                # 만일 목표한 x,y 좌표에 도착하면 해당 경로로 온 것이 가장 빠른 경로이므로 바로 이동값 리턴
                if x == n-1 and y == m-1:
                    return checker[x][y] 

    # 목표 x,y좌표에 도달하지 못하고 while문 종료
    # 목표좌표에 결국 도달할 수 없는 것으로, -1 리턴
    return -1



print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))