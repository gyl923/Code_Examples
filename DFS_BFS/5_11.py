#bfs 사용하며 탐색하며 조건에 맞는 다음칸 값 + 1

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
g = []
for i in range(n):
    g.append(list(map(int, input().rstrip())))
# print(g)
def bfs(a,b):
    queue = deque()
    queue.append([a,b])
    dir = [[1,0],[-1,0],[0,-1],[0,1]]
    while queue:
        a,b = queue.popleft()
        for i in dir:
            A = a+i[0]
            B = b+i[1]
            if A<0 or A>n-1 or B<0 or B>m-1:
                continue
            if g[A][B]==1:
                queue.append([A,B])
                g[A][B] = g[a][b]+1
    return g[n-1][m-1]
print(bfs(0,0))