#예제) 떡볶이 떡 만들기
'''
n개의 떡이 주어진다. n개의 떡 모두 일정길이h 만큼 자르고 남은 떡의 길이 합이 
m보다 크거나 같도록 만드는 h를 구하는 문제
'''

# 1
n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

def bs(arr,start,end,target):
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in arr:
            if i > mid:
                cnt += i-mid
        # if cnt == target:
        #     return mid
        if cnt < target:
            end = mid - 1
        else:
            ans = mid
            start = mid + 1
    return ans
ans = bs(arr,0,max(arr),6)
print(ans)

# 2
""" n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
start = 0
end = max(arr)
ans = 0
while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in arr:
            if i > mid:
                cnt += i-mid 
        if cnt < m:
            end = mid - 1
        else:
            ans = mid
            start = mid + 1
print(ans) """
