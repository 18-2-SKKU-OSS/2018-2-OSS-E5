## Sorting Algorithms

### 0. 선택 정렬
![3goa2af](https://user-images.githubusercontent.com/37110949/49509755-982cfc00-f8c9-11e8-83c1-050da5a03e43.png)

**선택 정렬** 은입력 목록을 두 부분으로 나눠 진행하는 알고리즘으로, 왼쪽에서 오른쪽으로 구성된 이미 정렬된 항목과 나머지 정렬되지 않은 항목으로 나뉜다. 처음에 정렬된 목록은 비어 있으며 정렬되지 않은 목록은 전체 입력 목록이다. 알고리즘은 정렬되지 않은 목록에서 가장 작은 요소(또는 정렬 순서에 따라 가장 큰 요소)를 찾아 가장 왼쪽에 정렬되지 않은 요소와 교환(스왑)하고 정렬된 목록의 경계를 오른쪽으로 이동함으로써 진행된다.

__시간 복잡도__
* 최악의 경우	O(n<sup>2</sup>)
* 최선의 경우	O(n<sup>2</sup>)
* 평균적인 경우	O(n<sup>2</sup>)

###### View the algorithm in [action](https://www.toptal.com/developers/sorting-algorithms/selection-sort)

### 1. Bubble Sort
![bubble-sort-in-c](https://user-images.githubusercontent.com/37110949/49448033-534a8c00-f81b-11e8-8b6a-78c83907ef7d.jpg)

**거품 정렬**은 목록을 반복적으로 통과하여 인접 쌍을 비교해 가면서 정렬하는 알고리즘이다. 목록의 통과는 스왑이 필요하지 않을 때까지 반복되며, 이는 목록이 정렬되었음을 나타낸다.

__시간 복잡도__
* 최악의 경우	O(n<sup>2</sup>)
* 최선의 경우	O(n)
* 평균적인 경우	O(n<sup>2</sup>)

###### View the algorithm in [action](https://www.toptal.com/developers/sorting-algorithms/bubble-sort)
