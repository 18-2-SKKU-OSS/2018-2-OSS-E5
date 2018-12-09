#!/usr/bin/python
# encoding=utf8

"""
트리나 그래프에서 한 루트로 탐색하다가 특정 상황에서 최대한 깊숙히 들어가서 확인한 뒤 
다시 돌아가 다른 루트로 탐색하는 방식이다. 대표적으로 백트래킹에 사용한다. 
일반적으로 재귀호출을 사용하여 구현하지만, 단순한 스택 배열로 구현하기도 한다. 
구조상 스택 오버플로우를 유의해야 한다.

갈림길이 나타날 때마다 '다른 길이 있다'는 정보만 기록하면서 자신이 지나간 길을 지워나간다. 
그러다 막다른 곳에 도달하면 직전 갈림길까지 돌아가면서 '이 길은 아님'이라는 표식을 남긴다. 
그렇게 갈림길을 순차적으로 탐색해 나가다 목적지를 발견하면 그대로 해답을 내고 종료.

단순 검색 속도 자체는 BFS에 비해서 느리다. 하지만 검색이 아닌 트래버스(traverse)를 할 경우는 많이 쓰인다. 
DFS는 특히 리프 노드에만 데이터를 저장하는 정렬 트리 구조에서 항상 순서대로 데이터를 방문한다는 장점이 있다. 
백트래킹에 사용되는 이유도 공통 상위를 가지는 아래 리프 노드들을 한방에 잘라 내 버리는게 가능하기 때문이다.
"""
""" Author: OMKAR PATHAK """
from __future__ import print_function


class Graph():
    def __init__(self):
        self.vertex = {}

    # 그래프 정점 인쇄용 
    def printGraph(self):
        print(self.vertex)
        for i in self.vertex.keys():
            print(i,' -> ', ' -> '.join([str(j) for j in self.vertex[i]]))

    # 두 정점 사이에 모서리 추가하기
    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present,
        if fromVertex in self.vertex.keys():
            self.vertex[fromVertex].append(toVertex)
        else:
            # else make a new vertex
            self.vertex[fromVertex] = [toVertex]

    def DFS(self):
        # 이미 방문한 노드를 저장하기 위해 방문한 배열
        visited = [False] * len(self.vertex)

        # 재귀 헬퍼 함수를 호출한다.
        for i in range(len(self.vertex)):
            if visited[i] == False:
                self.DFSRec(i, visited)

    def DFSRec(self, startVertex, visited):
        # 방문한 시점을 시작점으로 표시
        visited[startVertex] = True

        print(startVertex, end = ' ')

        # 이 노드에 인접한 모든 정점에 대해 반복
        for i in self.vertex.keys():
            if visited[i] == False:
                self.DFSRec(i, visited)

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.printGraph()
    print('DFS:')
    g.DFS()

    # OUTPUT:
    # 0  ->  1 -> 2
    # 1  ->  2
    # 2  ->  0 -> 3
    # 3  ->  3
    # DFS:
    # 0 1 2 3
