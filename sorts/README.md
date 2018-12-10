## Sorting Algorithms

### 0. 선택 정렬
![3goa2af](https://user-images.githubusercontent.com/37110949/49509755-982cfc00-f8c9-11e8-83c1-050da5a03e43.png)

**선택 정렬** 은입력 목록을 두 부분으로 나눠 진행하는 알고리즘으로, 왼쪽에서 오른쪽으로 구성된 이미 정렬된 항목과 나머지 정렬되지 않은 항목으로 나뉜다. 처음에 정렬된 목록은 비어 있으며 정렬되지 않은 목록은 전체 입력 목록이다. 알고리즘은 정렬되지 않은 목록에서 가장 작은 요소(또는 정렬 순서에 따라 가장 큰 요소)를 찾아 가장 왼쪽에 정렬되지 않은 요소와 교환(스왑)하고 정렬된 목록의 경계를 오른쪽으로 이동함으로써 진행된다.

__시간 복잡도__
* 최악의 경우 O(n<sup>2</sup>)
* 최선의 경우 O(n<sup>2</sup>)
* 평균적인 경우	O(n<sup>2</sup>)

###### View the algorithm in [action](https://www.toptal.com/developers/sorting-algorithms/selection-sort)

### 1. Bubble Sort
![bubble-sort-in-c](https://user-images.githubusercontent.com/37110949/49448033-534a8c00-f81b-11e8-8b6a-78c83907ef7d.jpg)

**거품 정렬**은 목록을 반복적으로 통과하여 인접 쌍을 비교해 가면서 정렬하는 알고리즘이다. 목록의 통과는 스왑이 필요하지 않을 때까지 반복되며, 이는 목록이 정렬되었음을 나타낸다.

__시간 복잡도__
* 최악의 경우 O(n<sup>2</sup>)
* 최선의 경우 O(n)
* 평균적인 경우	O(n<sup>2</sup>)

###### View the algorithm in [action](https://www.toptal.com/developers/sorting-algorithms/bubble-sort)

### 2. 삽입 정렬
![insertion-sort](https://user-images.githubusercontent.com/37110949/49484510-a99ae780-f87a-11e8-8681-981f5739e03d.png)

**삽입 정렬**은 최종 정렬된 배열을 한 번에 하나씩 구축하는 간단한 정렬 알고리즘이다. 이는 대규모 목록에서는 퀵 정렬, 힙 정렬 또는 합병 정렬과 같은 고급 알고리즘보다 훨씬 덜 효율적이다.

__시간 복잡도__
* 최악의 경우 O(n<sup>2</sup>)
* 최선의 경우 O(n)
* 평균적인 경우	O(n<sup>2</sup>)

###### View the algorithm in [action](https://www.toptal.com/developers/sorting-algorithms/insertion-sort)

### 3. 합병 정렬
![how merge sort algorithm works in java](https://user-images.githubusercontent.com/37110949/49570490-19dc6280-f97a-11e8-9d26-10540d5dcd88.png)

**합병 정렬**은 효율적인 범용 비교 기반 정렬 알고리즘이다. 대부분의 구현에서는 안정적인(stable) 정렬이 이루어지는데, 이는 항목의 순서가 입력과 출력에서 동일하다는 것을 의미한다. Mergeort는 1945년 John von Neumann에 의해 발명된 분할 및 정복 알고리즘이다.

__시간 복잡도__
* 최악의 경우 O(n log n)
* 최선의 경우 O(n log n)
* 평균적인 경우 O(n log n)

###### View the algorithm in [action](https://www.toptal.com/developers/sorting-algorithms/merge-sort)

### 4. 트리 정렬
![binary-search-tree-insertion-animation](https://user-images.githubusercontent.com/37110949/49629485-1229c600-fa2d-11e8-808a-875b37eba6af.gif)

**트리정렬**은 정렬할 요소에서 이진 검색 트리를 만든 다음 트리를 통과시켜 요소가 정렬된 상태로 나오도록 하는 정렬 알고리즘이다. 이것의 대표적인 용도는 온라인상에서 요소를 분류하는 것이다. 각 삽입 후 지금까지 본 요소 집합을 정렬된 순서대로 사용할 수 있다.

__시간 복잡도__
* 최악의 경우 O(n<sup>2</sup>)(unblanced), O(n log n)(blanced)
* 최선의 경우 O(n log n)
* 평균적인 경우 O(n log n)

### 5. 계수 정렬
![99279e365ab11c4934](https://user-images.githubusercontent.com/37110949/49685622-bee96d80-fb29-11e8-897f-66d459228ab7.png)

**계수 정렬** 은 컴퓨터 과학에서 작은 정수키에 따라 객체 집합을 정렬하는 알고리즘이다. 즉, 정수 정렬 알고리즘이다. 이는 각각의 뚜렷한 키 값이 있는 객체의 수를 세고, 출력 시퀀스에서 각 키 값의 위치를 결정하기 위해 그 카운트에 대한 산수를 사용하여 작동한다. 실행시간은 항목 수와 최대 키 값과 최소 키 값 간의 차이를 선형으로 나타내므로 키의 변동이 항목 수보다 크게 크지 않은 상황에서만 직접 사용할 수 있다. 그러나 더 큰 키를 더 효율적으로 처리할 수 있는 다른 정렬 알고리즘인 기수 정렬에서 서브루틴으로 자주 사용된다.

__시간 복잡도__
* 최악의 경우, 최선의 경우 O(n+k) k값에 의해 좌우
* 평균적인 경우	O(n+k)
