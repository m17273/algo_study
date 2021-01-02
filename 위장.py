# def solution(clothes):
#     from itertools import combinations

#     collection = {}
    

#     for i in range(len(clothes)):
#         function = clothes[i][1]
        
#         if function not in collection:
#             collection[function] = 1
#         else:
#             collection[function] += 1

#     answer = list(collection.values())
#     if len(answer) == 1:
#         return answer[0]
#     else:

#         total = 0
#         for i in range(len(answer)):
#             combi = list(combinations(answer, i+1))

#             for j in range(len(combi)):
#                 tmp = 1
#                 for k in range(len(combi[j])):
#                     tmp *= combi[j][k]
#                 total += tmp

#         return total
# 케이스 1번 통과 안됨(시간초과)


def solution(clothes):
    from itertools import combinations

    collection = {}
    

    for i in range(len(clothes)):
        function = clothes[i][1]
        
        if function not in collection:
            collection[function] = 1
        else:
            collection[function] += 1

    answer = list(collection.values())

    if len(answer) == 1:
        return answer[0]
    else:
        tmp = 1
        for i in answer:
            tmp *= i+1
        
        return tmp-1 #아무것도 안입은 경우 빼주기-모두 안입은 경우를 선택했을 시
