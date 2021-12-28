#예제) 부품찾기 (이진탐색)
'''
입력받은 n 개의 부품집합 A 중 
입력받은 m개의 부품들이 A 안에 존재 하는지 확인하는 프로그램
'''
def b_search(arr,start,end,target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

n = int(input())
arr = sorted(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))
for i in target:
    ans = b_search(arr,0,n-1,i)
    if ans == -1:
        print('no',end=' ')
    else:
        print('yes',end=' ')
