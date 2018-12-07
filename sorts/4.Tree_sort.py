"""
파이썬으로 Tree Sort를 구현한 코드입니다.
정확히 말하자면 Binary Search Tree를 구현하였습니다.
Binary Search Tree는 
    각 노드에 값이 있다.
    Root 노드가 존재한다.
    노드의 왼쪽 서브트리에는 그 노드의 값보다 작은 값들을 지닌 노드들로 이루어져있다.
    노드의 오른쪽 서브트리에는 그 노드의 값과 같거나 큰 값들을 지닌 노드들로 이루어져있다.
    좌우 하위 트리는 각각이 다시 Binary Search Tree 이어야 합니다.
"""

from __future__ import print_function

class node(): #Binary Search Tree를 구현한 class
    def __init__(self, val): #시작할때 처음 값을 node에 넣어줍니다.
        self.val = val
        self.left = None 
        self.right = None 
    
    def insert(self,val): #insert 해주는 코드로서 
        if self.val:
            if val < self.val:  #root의 값보다 작을 경우 왼쪽 서브트리로
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert(val)
            elif val > self.val: #root의 값보다 클 경우 오른쪽 서브트리로 넣어줍니다.
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val
"""
Binary Search Tree를 오름차순으로 출력하기위해선
inorder 순으로 배열에 저장하여 출력을 해야하기 위해 inorder 함수를 추가하였습니다.
"""
def inorder(root, res):  
    if root: 
        inorder(root.left,res)
        res.append(root.val)
        inorder(root.right,res)

def treesort(arr):
    # Binary Search Tree를 만드는 코드입니다.
    if len(arr) == 0:
        return arr
    root = node(arr[0])
    for i in range(1,len(arr)):
        root.insert(arr[i])
    # 오름차순 출력을 위해 inorder 함수를 사용하였습니다.
    res = []
    inorder(root,res)
    return res

if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
    for i in range(3):
        user_input = raw_input('Enter numbers separated by a comma:\n').strip()
        unsorted = [int(item) for item in user_input.split(',')]
        print(treesort(unsorted))
