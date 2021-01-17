import sys

N = int(sys.stdin.readline())
answer = [0]*31

for i in range(1, len(answer)):
    if i%2 == 0:
        answer[i] = 3*(i//2)


print(answer[N])


