# 거스름돈

n = 1260
cnt = 0

coin_type = [500,100,50,10]
for i in coin_type:
    cnt += n // i
    n %= i
print(cnt)