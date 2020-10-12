import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

graph = [[0]*n]*n
minimum_nium = 0
result = []


for i in range(n):
    if i != minimum:
        continue
    for j in range(i+1,n):
        minus = nums[j] - nums[i]
        if  minus <= 0:
            continue
        else:
            graph[i][j] = minus
            minimum_nium += min(graph[i])
    
    
    
    
    
    
    
    minimum = list(filter(lambda x : x>0, graph[i]))
    minimum_num += min(minimum)
    if len(minimum) != 0:
        result.append(graph[])

         






