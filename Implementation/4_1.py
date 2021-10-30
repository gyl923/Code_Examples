n = int(input())
x, y = 1, 1
arr = [[0,-1], [0,1], [-1,0], [1,0]]
dir = ['L', 'R', 'U', 'D']
des = input().split()
for i in des:
    for j in range(len(dir)):
        if i == dir[j]:
            if x+arr[j][1]>=1 and y+arr[j][0]>=1 and x+arr[j][1]<=n and y+arr[j][0]<=n:
                x += arr[j][1]
                y += arr[j][0]
            break
print(y,x)
