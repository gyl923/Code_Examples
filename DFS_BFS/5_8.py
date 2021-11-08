# DFS 깊이우선탐색
# DFS 메서드 정의 => 스택 구조
def dfs(g , v, visited):
    #현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in g[v]:
        if not visited[v]:
            dfs(g, i, visited)
    
#각 노드에 연결된 다른 노드를 리스트 자료형으로 표현(2차원 리스트)
g = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8]
    [1,7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9
#정의된 DFS함수 호출
dfs(g, 1, visited)