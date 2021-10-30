# n x n 범위 밖은 나가지 않는다는 전제

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A,B,d = map(int, input().split())

cnt, cnt_l = 1,0
dir = [[-1,0],[0,1],[1,0],[0,-1]]
arr = []
destinaion = [[0]*n for _ in range(n)]
destinaion[A][B] = 1
for i in range(n):
    arr.append(list(map(int, input().split())))

def turn_l(n):
    n-=1
    if n < 0:
        n = 3
    return n

while(True):
    d = turn_l(d)
    if arr[A+dir[d][0]][B+dir[d][1]]==0 and  destinaion[A+dir[d][0]][B+dir[d][1]] == 0:
        cnt_l = 0 
        A += dir[d][0]
        B += dir[d][1]
        destinaion[A][B] = 1
        cnt += 1
    else :
        cnt_l += 1
        if cnt_l == 4:
            cnt_l = 0
            if destinaion[A-dir[d][0]][B-dir[d][1]]==0:
                A -= dir[d][0]
                B -= dir[d][1]
            else :
                break
print(cnt)

