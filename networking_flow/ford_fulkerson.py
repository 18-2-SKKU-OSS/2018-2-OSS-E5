# Ford-Fulkerson Algorithm
"""
Ford-Fulkerson 방법 또는 Ford-Fulkerson 알고리즘 (FFA)은 
흐름 네트워크에서 최대 흐름을 계산하는 greedy 알고리즘입니다. 
이는 잔여 그래프에서 증가 경로를 찾는 접근법이 완전히 지정되지 않았거나
다른 실행 시간을 가진 여러 구현에서 지정되기 때문에 "알고리즘"대신 "방법"이라고도 합니다.

기술:
     (1) 초기 흐름을 0으로 시작합니다.
     (2) 소스에서 싱크까지 증가 경로를 선택하고 흐름 경로를 추가하십시오.
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
     
def FordFulkerson(graph, source, sink):
    #이 배열은 BFS로써 인덱스를 쌓아가며 저장소 경로로서 채워집니다.
    parent = [-1]*(len(graph))
    max_flow = 0 
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
    return max_flow

graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10 ,12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

source, sink = 0, 5
print(FordFulkerson(graph, source, sink))
