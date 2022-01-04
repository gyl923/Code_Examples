
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