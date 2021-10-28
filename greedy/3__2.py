# 큰 수의 법칙

n,m,k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
first = arr[0]
second = arr[1]
cnt = m%k
print(cnt*second + (m-cnt)*first)

#1
""" arr.sort(reverse=True)
cnt,ans = 0,0
for i in range(m-(m%k)):
    ans += arr[0]
    cnt+=1
    if cnt == k:
        ans += arr[1]
        cnt=0
print(ans)
 """
