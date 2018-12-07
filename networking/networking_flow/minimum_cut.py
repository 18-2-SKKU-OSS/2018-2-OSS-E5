# Ford_Fulkerson 알고리즘의 최소 절단.

"""
※시작점과 거리가 멀수록 탐색이 느려진다. 하지만 근처에 있을 경우 빠르게 탐색 가능하다.

BFS에서는 루트에서 시작하여 둘째 층을 왼쪽에서 오른쪽으로 훑어나가고, 
그 다음 층을 또 왼쪽 에서 오른쪽으로 훑어나가는 식으로 검색을 한다. 
원하는 노드를 찾거나 모든 노드를 다 확인해보고 나면 검색이 끝난다. 
노드를 찾아내는 데 걸리는 시간은 O(n)이기 때문에 큰 트리에 대해서는 이런식으로 검색을 하지 않는 것이 좋다. 
BFS에서는 어떤 층을 검색할 때 그층에 있는 모든 노드의 자식 노드를 저장해둬야 하기 때문에,
메모리도 꽤 많이 사용해야 한다.
"""
    
def BFS(graph, s, t, parent):
    # 반복되지 않은 노드가 있으면 True를 반환합니다.
    visited = [False]*len(graph)
    queue=[]
    queue.append(s)
    visited[s] = True
    
    while queue:
        u = queue.pop(0)
        for ind in range(len(graph[u])):
            if visited[ind] == False and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[t] else False
 
def mincut(graph, source, sink):
    # 이 배열은 BFS로써 인덱스를 쌓아가며 저장소 경로로서 채워집니다.
    parent = [-1]*(len(graph))
    max_flow = 0 
    res = []
    temp = [i[:] for i in graph]   # 원본 오려두기, 사본을 기록하십시오.
    while BFS(graph, source, sink, parent) :
        path_flow = float("Inf")
        s = sink

        while(s !=  source):
            # 선택 경로에서 최소값 찾기
            path_flow = min (path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow +=  path_flow
        v = sink
        
        while(v !=  source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0 and temp[i][j] > 0:
                res.append((i,j))

    return res

graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10 ,12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

source, sink = 0, 5
print(mincut(graph, source, sink))
