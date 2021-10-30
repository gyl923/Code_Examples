data = input()

move = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
x,y= ord(data[0]) - ord('a')+1, int(data[1])

cnt=0
for i in move:
    if x+i[1] <= 8 and x+i[1] >= 1 and y+i[0] <= 8 and y+i[0] >= 1:
        cnt+=1
print(cnt)
