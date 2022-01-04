# 다이나믹프로그래밍 예제
'''
효율적인 화폐 구성
n가지 종류의 화폐
m원이 되도록 조합하여 사용되는 최소한의 화폐갯수 구하기
불가능한 경우 -1
input       output
2 15        5
2 
3
'''
n,m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
d = [1001]*(m+1)
d[0] = 0

for k in arr:
    for i in range(k,m+1):
        if d[i-k] != 1001:
            d[i] = min(d[i],d[i-k]+1)
if d[m] == 1001:
    print(-1)
else:
    print(d[m])