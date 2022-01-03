# 다이나믹프로그래밍 예시 피보나치수열
# 반복문으로 구현 + 메모이제이션 / 보텀업(상향식)

d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])
