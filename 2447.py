import sys

N = int(sys.stdin.readline())

def starMaker():
    cnt = 0
    while cnt<9:
        print('*', end='')
        cnt += 1

        if cnt% 3 == 0 :
            print()
        if cnt == 
            print(' ', end='')
            cnt += 1
        
def Stars(N):
    cnt = 0
    while cnt < (N*N):
        starMaker()
        

Stars(N)