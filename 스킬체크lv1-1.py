def solution(n):
    new = list(str(n))
    
    new= sorted(new, reverse=True)
    answer = ''.join(new)
    return int(answer)
solution(118372)