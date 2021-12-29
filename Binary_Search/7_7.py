#예제) 부품찾기 (set() 집합 사용) -> 가장 효율적
'''
입력받은 n 개의 부품집합 A 중 
입력받은 m개의 부품들이 A 안에 존재 하는지 확인하는 프로그램
'''
n = int(input())
arr = set(map(int,input().split()))
m = int(input())
target = list(map(int, input().split()))
for i in target:
    if i not in arr:
        print('no',end=' ')
    else:
        print('yes',end=' ')