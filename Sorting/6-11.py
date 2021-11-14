# 예제 3 성적이 낮은 순서로 학생 출력하기

import sys
input = sys.stdin.readline
arr = []
for _  in range(int(input())):
    a,b = input().split()
    arr.append((a,b))
arr.sort(key=lambda x: x[1])
for i in arr:
    print(i[0],end=' ')
    