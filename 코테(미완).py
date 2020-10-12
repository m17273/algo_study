import math

def solution(w,h):
    rectangle = w*h
    lean = h/w
    height = []
    result_list = []
    cnt = 0
    
    

    for i in range(1,w+1):

        line = lean * i
        result = math.ceil(line)
        result_list.append(result)

        if line < result:
            cnt += result
            height.append(line)
        if line == result:
            if lean == line:
                cnt += 1
            else:
                cnt += math.ceil(line - height[-1])

                    
                
    
    return (rectangle-cnt)

print(solution(8,12))
            