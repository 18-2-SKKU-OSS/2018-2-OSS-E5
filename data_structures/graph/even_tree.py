"""
트피 (주기가없는 간단한 연결 그래프)가 주어집니다. 트리는 1에서 N까지 번호가 매겨진 N 개의 노드를 가지며 노드 1을 루팅합니다.

포리스트의 연결된 각 구성 요소에 짝수 개의 노드가 포함되도록 포리스트를 얻기 위해 트리에서 제거 할 수있는 최대 edge 수를 찾습니다.

제약 조건
2 <= 2 <= 100

주 : 트리 입력은 항상 짝수 개의 노드를 포함하는 구성 요소로 분해 될 수 있습니다.
"""
from __future__ import print_function
# pylint: disable=invalid-name
from collections import defaultdict


def dfs(start):
    """DFS traversal"""
    # pylint: disable=redefined-outer-name
    ret = 1
    visited[start] = True
    for v in tree.get(start):
        if v not in visited:
            ret += dfs(v)
    if ret % 2 == 0:
        cuts.append(start)
    return ret


def even_tree():
    """
    2 1
    3 1
    4 3
    5 2
    6 1
    7 2
    8 6
    9 8
    10 8
    edge (1,3) 및 (1,6)을 제거하면 원하는 결과인 2를 얻을 수 있습니다 
    """
    dfs(1)


if __name__ == '__main__':
    n, m = 10, 9
    tree = defaultdict(list)
    visited = {}
    cuts = []
    count = 0
    edges = [
        (2, 1),
        (3, 1),
        (4, 3),
        (5, 2),
        (6, 1),
        (7, 2),
        (8, 6),
        (9, 8),
        (10, 8),
    ]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    even_tree()
    print(len(cuts) - 1)
