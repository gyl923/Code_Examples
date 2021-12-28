#예제) 부품찾기 (계수정렬)
'''
입력받은 n 개의 부품집합 A 중 
입력받은 m개의 부품들이 A 안에 존재 하는지 확인하는 프로그램
'''
arr = [0] * 1000001
n = int(input())
for i in input().split():
    arr[int(i)] = 1

m = int(input())
target = list(map(int, input().split()))

for i in target:
    if arr[i] == 1:
        print('yes',end=' ')
    else:
        print('no',end=' ')
