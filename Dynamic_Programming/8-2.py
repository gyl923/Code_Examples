# 다이나믹프로그래밍 예시 피보나치수열
# 재귀함수로 구현 + 메모이제이션

# 메모이제이션을 위한 리스트 초기화
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]
print(fibo(99))
