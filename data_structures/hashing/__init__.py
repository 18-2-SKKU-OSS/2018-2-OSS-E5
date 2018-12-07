"""
원래 주소로부터 1, 4, 9, 16, …과 같이 2차로 되는 거리만큼 떨어진 곳을 
차례로 탐색하여 맨 처음에 나오는 빈 곳에 집어넣는데, 해싱(hashing)에 있어서 
같은 키값을 갖는 2개의 엔트리가 충돌한 경우에 이것을 해소하는 한 방법이다.
2차 탐색 [quadratic probing]
"""
from .hash_table import HashTable

class QuadraticProbing(HashTable):

    def __init__(self):
        super(self.__class__, self).__init__()
