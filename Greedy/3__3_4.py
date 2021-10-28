# 숫자 카드 게임
# 행마다 min을 뽑아 비교
# 그중 max인것을 찾아 선택

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)] # m개씩 입력
cnt=0
for i in range(n):
    cnt = max(cnt, min(arr[i]))
print(cnt)