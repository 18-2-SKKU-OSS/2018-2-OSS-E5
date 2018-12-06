'''
A binary search Tree
이진 탐색 트리입니다.
'''
from __future__ import print_function
class Node:

    def __init__(self, label, parent):
        self.label = label
        self.left = None
        self.right = None
        # 노드를 쉽게 삭제하기 위해 추가됨
        self.parent = parent

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, label):
        # 새 노드 생성
        new_node = Node(label, None)
        # 만약 트리가 비었다면 
        if self.empty():
            self.root = new_node
        else:
            # 만약 트리가 비어있지 않다면
            curr_node = self.root
            # 모든 자식노드를 다 돌 때까지 
            while curr_node is not None:
                # 부모노드의 참조를 유지한다.
                parent_node = curr_node
                # 라벨에 있는 값이 현재 노드보다 작다면
                if new_node.getLabel() < curr_node.getLabel():
                # 왼쪽 자식 노드로 이동한다.
                    curr_node = curr_node.getLeft()
                else:
                    # 그렇지 않은 경우 오른쪽 자식 노드로 이동한다.
                    curr_node = curr_node.getRight()
            # 자식 노드로서 새 노드를 삽입해야 하는 경우
            if new_node.getLabel() < parent_node.getLabel():
                parent_node.setLeft(new_node)
            else:
                parent_node.setRight(new_node)
            # 새 노드에 부모 노드로서 지정
            new_node.setParent(parent_node)      
    
    def delete(self, label):
        if (not self.empty()):
            # 라벨값을 갖고 있는 노드를 찾기
            node = self.getNode(label)
            # 만약 노드가 존재한다면
            if(node is not None):
                # 만약 자식 노드가 없다면
                if(node.getLeft() is None and node.getRight() is None):
                    self.__reassignNodes(node, None)
                    node = None
                # 만약 오른쪽 자식 노드만 있다면
                elif(node.getLeft() is None and node.getRight() is not None):
                    self.__reassignNodes(node, node.getRight())
                # 만약 왼쪽 자식 노드만 있다면
                elif(node.getLeft() is not None and node.getRight() is None):
                    self.__reassignNodes(node, node.getLeft())
                # 만약 양쪽 자식 노드가 있다면
                else:
                    # 그 라벨보다 작은 값들 중에 가장 큰 값을 찾아낸다.
                    tmpNode = self.getMax(node.getLeft())
                    # tempnode를 지운다.
                    self.delete(tmpNode.getLabel())
                    # 트리 구조를 유지하기 위해 temp노드의 라벨에 대해 setlabel 을 수행
                    node.setLabel(tmpNode.getLabel())
    
    def getNode(self, label):
        curr_node = None
        # 만약 트리가 비어 있지 않다면
        if(not self.empty()):
            # 루트 노드를 가져와서
            curr_node = self.getRoot()
            # 우리가 찾아내야 하는 노드를 찾을 수 없을 때 까지
            # NoneType Attribute error가 안나게 하기 위해 lazy computation을 수행
            while curr_node is not None and curr_node.getLabel() is not label:
                # 만약 라벨값이 현재 노드보다 작다면
                if label < curr_node.getLabel():
                    # 왼쪽 자식 노드로 이동
                    curr_node = curr_node.getLeft()
                else:
                    # 그렇지 않은 경우 오른쪽 자식 노드로 이동
                    curr_node = curr_node.getRight()
        return curr_node

    def getMax(self, root = None):
        if(root is not None):
            curr_node = root
        else:
            # 오른쪽 가지로 깊게 진행
            curr_node = self.getRoot()
        if(not self.empty()):
            while(curr_node.getRight() is not None):
                curr_node = curr_node.getRight()
        return curr_node

    def getMin(self, root = None):
        if(root is not None):
            curr_node = root
        else:
            # 왼쪽 가지고 깊게 진행
            curr_node = self.getRoot()
        if(not self.empty()):
            curr_node = self.getRoot()
            while(curr_node.getLeft() is not None):
                curr_node = curr_node.getLeft()
        return curr_node

    def empty(self):
        if self.root is None:
            return True
        return False

    def __InOrderTraversal(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList.insert(0, curr_node)
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getLeft())
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getRight())
        return nodeList

    def getRoot(self):
        return self.root

    def __isRightChildren(self, node):
        if(node == node.getParent().getRight()):
            return True
        return False

    def __reassignNodes(self, node, newChildren):
        if(newChildren is not None):
            newChildren.setParent(node.getParent())
        if(node.getParent() is not None):
            # 만약 이것이 오른쪽 자식 노드면
            if(self.__isRightChildren(node)):
                node.getParent().setRight(newChildren)
            else:
                # 만약 이것이 왼쪽 자식 노드면
                node.getParent().setLeft(newChildren)

    # 이 함수는 트리를 서치하는 함수입니다. 초기값은
    # inorder 순회입니다. 순회 함수로 전달할 수 있으며
    # client 코드로서 필요한 트리
    def traversalTree(self, traversalFunction = None, root = None):
        if(traversalFunction is None):
            # 디폴트 값으로 preorder 트리의 내역을 출력
            return self.__InOrderTraversal(self.root)
        else:
            # 사용가 원하는 방식으로 트리의 내력을 출력
            return traversalFunction(self.root)

    # 리스트에 있는 모든 라벨들을 출력 
    #In Order 순회
    def __str__(self):
        list = self.__InOrderTraversal(self.root)
        str = ""
        for x in list:
            str = str + " " + x.getLabel().__str__()
        return str

def InPreOrder(curr_node):
    nodeList = []
    if curr_node is not None:
        nodeList = nodeList + InPreOrder(curr_node.getLeft())
        nodeList.insert(0, curr_node.getLabel())
        nodeList = nodeList + InPreOrder(curr_node.getRight())
    return nodeList

def testBinarySearchTree():
    '''
    예시
                  8
                 / \
                3   10
               / \    \
              1   6    14
                 / \   /
                4   7 13 
    '''

    '''
    삭제 후의 예시
                  7
                 / \
                1   4

    '''
    t = BinarySearchTree()
    t.insert(8)
    t.insert(3)
    t.insert(6)
    t.insert(1)
    t.insert(10)
    t.insert(14)
    t.insert(13)
    t.insert(4)
    t.insert(7)

    #in order traversal 을 이용한 모든 리스트 원소 출력
    print(t.__str__())

    if(t.getNode(6) is not None):
        print("The label 6 exists")
    else:
        print("The label 6 doesn't exist")

    if(t.getNode(-1) is not None):
        print("The label -1 exists")
    else:
        print("The label -1 doesn't exist")
    
    if(not t.empty()):
        print(("Max Value: ", t.getMax().getLabel()))
        print(("Min Value: ", t.getMin().getLabel()))
    
    t.delete(13)
    t.delete(10)
    t.delete(8)
    t.delete(3)
    t.delete(6)
    t.delete(14)

    # pre order을 이용한 트리 안에 있는 모든 원소들을 출력
    # 그리고 출력
    list = t.traversalTree(InPreOrder, t.root)
    for x in list:
        print(x)

if __name__ == "__main__":
    testBinarySearchTree()
