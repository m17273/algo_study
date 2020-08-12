import sys

n, m = map(int, sys.stdin.readline().split())

tomato_box = []
graph_count = []

for _ in range(m):
    tomato = list(map(int, sys.stdin.readline().split()))
    tomato.insert(0, -1)
    tomato.insert(len(tomato), -1)
    tomato_box.append(tomato)


tomato_box.insert(0, [-1]*(n+2))
tomato_box.insert(len(tomato_box), [-1]*(n+2))
        
for _ in range(m+2):
    graph_count.append([0]*(n+2))

def BFS(tomato_box, graph_count,m,n):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = []
    result = []

    for i in range(1, m+1):
        for j in range(1, n+1):
            if tomato_box[i][j] == 1:
                queue.append([i,j])
                graph_count[i][j] = 1
            elif tomato_box[i][j] == -1:
                graph_count[i][j] = -1
            '''
            elif tomato_box[i][j] == 0 and tomato_box[i+1][j] == -1 and tomato_box[i-1][j] == -1 and tomato_box[i][j+1] == -1 and tomato_box[i][j-1] == -1:
                return -1
            '''
                
    
    while queue:
        numx = queue[0][0]
        numy = queue[0][1]

        queue.pop(0)

        for i in range(4):
            x = numx + dx[i]
            y = numy + dy[i]

            if tomato_box[x][y] == 0 and graph_count[x][y] == 0 and [x,y] not in queue:
                graph_count[x][y] = graph_count[numx][numy] + 1
                queue.append([x,y])

                '''
                if graph_count[x][y] not in result:
                    result.append(graph_count[x][y])
                '''

    for i in range(1, m+1):
        for j in range(1, n+1):
            if graph_count[i][j] == 0:
                return -1
            else:
                if graph_count[i][j] not in result:
                    result.append(graph_count[i][j])

    if len(result) == 0:
        return 0
    else:
        result.sort()
        return result[-1]-1


print(BFS(tomato_box, graph_count,m,n))