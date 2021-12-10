def sequential_search(n,target,arr):
    for i in range(n):
        if arr[i] == target:
            return i+1
            
print('생성할 원소수와 찾으려는 이름을 공백포함하여 입력')
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print('원소 개수만큼 문자열 입력. 구분은 공백 한칸.')
arr = input().split()
print(sequential_search(n,target,arr))