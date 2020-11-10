def solution(number,k):
    stack = []
    number_int = list(number)
    
   
    for i in range(len(number_int)):
        stack.append(number_int[i])
        while stack:

