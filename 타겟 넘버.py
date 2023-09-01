# bfs/dfs가 아닌 리스트로 통과
# 주어진 수를 통해 생성 가능한 모든 노드를 배열에 집어넣은 후 count함수를 통해 target 갯수를 리턴
def solution(numbers, target):
    arr = [0]

    for i in numbers:
        temp = []

        for j in arr:
            temp.append(j+i)
            temp.append(j-i)
        # temp 리스트의 값을 arr로 복사
        #[:] -> 리스트 전체 복사
        # arr = temp해도 값은 동일한데, 왜 굳이 복사를 해야하는 지는 잘 모르겠음
        arr = temp[:]

    return arr.count(target)

print(solution([1,1,1,1,1],3))
