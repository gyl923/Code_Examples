# 1이 될 때까지

n,k = map(int,input().split())
ans = 0

while(n > 1):
    if n%k!=0:
        n -= 1
    else:
        n //= k
    ans += 1
print(ans)