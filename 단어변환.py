def solution(begin, target, words):
    answer = [begin]
    cnt = 0

    if target not in words:
        return 0
    
    while True:
        for word in answer:
            tmp = []
            for i in words:
                different = 0
                for j in range(len(word)):
                    
                    if i[j] != word[j]:
                        different += 1
                    if different > 1:
                        break
                if different == 1:
                    tmp.append(i)
                    words.remove(i)

        cnt += 1
        if target in tmp:
            return cnt
        answer = tmp

solution('hit','cog',['hot', 'dot', 'dog', 'lot', 'log', 'cog'])
# 내힘으로 한게 하나두 없는 코드..현타온다..ㅠ.




