# 칸의 알고리즘은 BFS를 사용하여 지시 된 비주기 그래프의 위상 적 순서를 찾는 데 사용됩니다
def topologicalSort(l):
    indegree = [0] * len(l)
    queue = []
    topo = []
    cnt = 0

    for key, values in l.items():
        for i in values:
            indegree[i] += 1

    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    while(queue):
        vertex = queue.pop(0)
        cnt += 1
        topo.append(vertex)
        for x in l[vertex]:
            indegree[x] -= 1
            if indegree[x] == 0:
                queue.append(x)

    if cnt != len(l):
        print("Cycle exists")
    else:
        print(topo)

# 인접 그래프 목록
l = {0:[1,2], 1:[3], 2:[3], 3:[4,5], 4:[], 5:[]}
topologicalSort(l)
