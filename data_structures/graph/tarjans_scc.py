from collections import deque


def tarjan(g):
    """
     유향 그래프에서 강하게 연결된 구성 요소를 찾는 데 필요한 Tarjan의 알고리즘

     도달 가능성, 구성 요소 내의 해당 노드 색인 (색인) 및 
     해당 노드에서 도달 할 수있는 가장 낮은 색인 (하위 링크)을 
     추적하기 위해 각 노드의 두 가지 주요 속성을 사용합니다.

     그런 다음 각 구성 요소의 dfs를 수행하여 각 노드에 대해 
     이러한 매개 변수를 업데이트하고 방문하는 노드를 저장합니다.

     현재 노드에서 도달 할 수있는 가장 낮은 노드가 현재 노드의 
     인덱스와 같은 경우 강하게 연결된 구성 요소의 루트 여야하며 
     저장하기 때문에 강하게 연결된 구성 요소로 도달 가능한 정점을 얻습니다.

     복잡성 : strong_connect ()는 각 노드에 대해 
     한 번만 호출되며 DFS이므로 O (| E |)의 복잡성이 있습니다.
     
     따라서 이것은 그래프 G = (V, E)에 대한 복잡도 O (| V | + | E |)를 갖습니다.

    """

    n = len(g)
    stack = deque()
    on_stack = [False for _ in range(n)]
    index_of = [-1 for _ in range(n)]
    lowlink_of = index_of[:]

    def strong_connect(v, index, components):
        index_of[v] = index  #이 노드를 볼 때 번호
        lowlink_of[v] = index  # 여기에서 도달 할 수있는 최저 등급 노드
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in g[v]:
            if index_of[w] == -1:
                index = strong_connect(w, index, components)
                lowlink_of[v] = lowlink_of[w] if lowlink_of[w] < lowlink_of[v] else lowlink_of[v]
            elif on_stack[w]:
                lowlink_of[v] = lowlink_of[w] if lowlink_of[w] < lowlink_of[v] else lowlink_of[v]

        if lowlink_of[v] == index_of[v]:
            component = []
            w = stack.pop()
            on_stack[w] = False
            component.append(w)
            while w != v:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
            components.append(component)
        return index

    components = []
    for v in range(n):
        if index_of[v] == -1:
            strong_connect(v, 0, components)

    return components


def create_graph(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    return g


if __name__ == '__main__':
    # 테스트
    n_vertices = 7
    source = [0, 0, 1, 2, 3, 3, 4, 4, 6]
    target = [1, 3, 2, 0, 1, 4, 5, 6, 5]
    edges = [(u, v) for u, v in zip(source, target)]
    g = create_graph(n_vertices, edges)

    assert [[5], [6], [4], [3, 2, 1, 0]] == tarjan(g)
