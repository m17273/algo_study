def solution(s):
    tmp = s[2:len(s)-2]
    tmp_ = tmp.split('},{')
    answer = []
    
    new = sorted(tmp_, key = len)

    for word in new:
        tmp_word = list(word.split(','))
        
        for word in tmp_word:
            if int(word) not in answer:
                answer.append(int(word))

    return answer
