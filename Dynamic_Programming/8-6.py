# 다이나믹프로그래밍 예제
'''
<개미전사>
식량창고 터는데 최대한 많이터는 경우
인접식량창고 털면 걸린다.
n개의 창고, arr의 식량의 양
'''
n = int(input())
arr = list(map(int, input().split()))
ans = [0]*len(arr)
ans[0] = arr[0]
ans[1] = max(arr[1],arr[0])
for i in range(2,n):
    ans[i] = max(ans[i-1],ans[i-2]+arr[i])
print(ans[-1])