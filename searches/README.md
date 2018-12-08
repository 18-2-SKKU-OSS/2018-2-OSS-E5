## 탐색 알고리즘

### 1. 선형 탐색
![1 linear_search](https://user-images.githubusercontent.com/38908132/49684284-54c6cd80-fb15-11e8-946a-290519ac5588.gif)

**선형 탐색** 또는 순차 탐색은 목록 내의 대상을 찾는 방법입니다. 찾는 값과 요소의 값이 일치하거나 모든 요소가 검색 될 때까지 목록의 요소 값에 대해 순차적으로 탐색합니다. 선형 검색은 최악의 시간복잡도 내에서 움직이며 최대 n 개의 비교를 수행합니다. 여기서 n은 목록의 길이입니다.

__Properties__
* 최악의 경우	O(n)
* 최선의 경우	O(1)
* 평균적인 경우	O(n)
* 최악의 경우(공간)	O(1)

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Linear_search)

### 2. 이진 탐색
![2 binary_search](https://user-images.githubusercontent.com/38908132/49684281-54c6cd80-fb15-11e8-8d9a-d3928cea5afa.png)

**이진 탐색**은 반 간격 검색 또는 로그 검색이라고도 하는 이진 검색은 정렬된 배열 내에서 대상 값의 위치를 찾는 탐색 알고리즘입니다. 목표 값을 배열의 중간 요소와 비교하여 동일하지 않으면, 절반을 배제한 상태로 다시 성공할 때까지 나머지 절반의 탐색을 진행합니다.

__Properties__
* 최악의 경우	O(log n)
* 최선의 경우	O(1)
* 평균적인 경우	O(log n)
* 최악의 경우(공간)	O(1)

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)

## 3. 보간 탐색

**보간 탐색**는 배열에서 키에 할당된 숫자 값(키 값)으로 정렬된 키를 검색하는 알고리즘이다. 이 알고리즘은 1957년에 W. W. Peterson에 의해 처음 묘사되었다. 보간 탐색은 사람들이 전화 디렉토리에서 이름을 검색하는 방법(책의 항목을 정렬하는 키 값)과 유사하다: 각 단계에서 알고리즘은 검색 공간의 경계에 있는 키 값과 원하는 키의 값에 기초하여 검색된 항목이 있을 수 있는 나머지 검색 공간의 위치를 선형 보간법을 통해 계산한다. 이 추정된 위치에서 실제로 발견된 키 값을 찾고 있는 키 값과 비교한다. 동일하지 않으면 비교에 따라 나머지 검색 공간은 추정 위치 이전 또는 이후 부품으로 축소된다. 이 방법은 키 값 사이의 차이 크기에 대한 계산이 합리적인 경우에만 작동한다.

이에 비해 이진 탐색은 항상 남은 검색 공간의 중간을 선택하고, 추정된 위치에서 찾은 키와 탐색한 키 간의 비교에 따라 한 쪽 또는 다른 쪽 검색 공간을 버린다. 키에 대한 숫자 값은 필요 없고, 전체 순서만 필요하다. 나머지 검색 공간은 추정 위치 이전 또는 이후 부품으로 축소된다. 선형 탐색은 정렬을 무시하면서 시작부터 요소를 하나씩 비교하는 경우에만 평등을 사용한다.

__Properties__
* 최악의 경우	O(n)
* 평균적인 경우	O(log log n)

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Interpolation_search)

## 4. Jump Search
![4 jump_search](https://user-images.githubusercontent.com/38908132/49684282-54c6cd80-fb15-11e8-98b3-e3a9108ddf83.jpg)

**Jump search** or block search refers to a search algorithm for ordered lists. It works by first checking all items L<sub>km</sub>, where ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/2a5bc4b7383031ba693b7433198ead7170954c1d)  and *m* is the block size, until an item is found that is larger than the search key. To find the exact position of the search key in the list a linear search is performed on the sublist L<sub>[(k-1)m, km]</sub>.

The optimal value of m is √n, where n is the length of the list L. Because both steps of the algorithm look at, at most, √n items the algorithm runs in O(√n) time. This is better than a linear search, but worse than a binary search. The advantage over the latter is that a jump search only needs to jump backwards once, while a binary can jump backwards up to log n times. This can be important if a jumping backwards takes significantly more time than jumping forward.

The algorithm can be modified by performing multiple levels of jump search on the sublists, before finally performing the linear search. For an k-level jump search the optimum block size m<sub>l</sub> for the l<sup>th</sup> level (counting from 1) is n<sup>(k-l)/k</sup>. The modified algorithm will perform *k* backward jumps and runs in O(kn<sup>1/(k+1)</sup>) time.

__Properties__
* Worst case performance	O(sqrt n)
* Best case performance	O(1)
* Average case performance	O(sqrt n)
* Space complexity O(1)

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Jump_search)

## 5. Quick Select Search
![5 quick_search](https://user-images.githubusercontent.com/38908132/49684283-54c6cd80-fb15-11e8-802f-257c4f85c5fb.gif)

**Quickselect** is a selection algorithm to find the kth smallest element in an unordered list. It is related to the quicksort sorting algorithm. Like quicksort, it was developed by Tony Hoare, and thus is also known as Hoare's selection algorithm. Like quicksort, it is efficient in practice and has good average-case performance, but has poor worst-case performance. Quickselect and its variants are the selection algorithms most often used in efficient real-world implementations.

As with quicksort, quickselect is generally implemented as an in-place algorithm, and beyond selecting the k'th element, it also partially sorts the data. See selection algorithm for further discussion of the connection with sorting.

__Properties__
* Worst case performance	O(n)
* Average case performance	O(log n)

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Quickselect)

## 6. Fibonacci Search
![fibsearch31-660x578](https://user-images.githubusercontent.com/38908132/49605746-b7648000-f9d4-11e8-8d08-6879863aa30b.png)
 
 **Fibonacci search** technique is a method of searching a sorted array using a divide and conquer algorithm that narrows down possible locations with the aid of Fibonacci numbers.[1] Compared to binary search where the sorted array is divided into two equal-sized parts, one of which is examined further, Fibonacci search divides the array into two parts that have sizes that are consecutive Fibonacci numbers.

__Properties__
* Worst case performance	O(log n)
* Average case performance	O(log n)

 ###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_search_technique)
 
## 7. Exponential Search
 **exponential search** (also called doubling search or galloping search or Struzik search) is an algorithm, created by Jon Bentley and Andrew Chi-Chih Yao in 1976, for searching sorted, unbounded/infinite lists. There are numerous ways to implement this with the most common being to determine a range that the search key resides in and performing a binary search within that range. 
 The idea is to start with subarray size 1, compare its last element with x, then try size 2, then 4 and so on until last element of a subarray is not greater. Once we find an index i (after repeated doubling of i), we know that the element must be present between i/2 and i (Why i/2? because we could not find a greater value in previous iteration)
 __Properties__
* Worst case performance	O(log n)
* Average case performance	O(log n)
 ###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Exponential_search)
 
## 8. Ternary Search
 **Ternary Search** algorithm is a technique in computer science for finding the minimum or maximum of a unimodal function. A ternary search determines either that the minimum or maximum cannot be in the first third of the domain or that it cannot be in the last third of the domain, then repeats on the remaining third. A ternary search is an example of a divide and conquer algorithm (see search algorithm).
 Assume we are looking for a maximum of f(x) and that we know the maximum lies somewhere between A and B. For the algorithm to be applicable, there must be some value x such that
 for all a,b with A ≤ a < b ≤ x, we have f(a) < f(b), and
 for all a,b with x ≤ a < b ≤ B, we have f(a) > f(b).
 __Properties__
* Average case performance	O(log 3n)
* Space Complexity O(1)
 ###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Ternary_search)
 
## Tabu Search
Tabu search uses a local or neighborhood search procedure to iteratively move from one potential solution ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) to an improved solution ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/0ac74959896052e160a5953102e4bc3850fe93b2) in the neighborhood of ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4), until some stopping criterion has been satisfied (generally, an attempt limit or a score threshold). Local search procedures often become stuck in poor-scoring areas or areas where scores plateau. In order to avoid these pitfalls and explore regions of the search space that would be left unexplored by other local search procedures, tabu search carefully explores the neighborhood of each solution as the search progresses. The solutions admitted to the new neighborhood, ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/4db1b4a2cfa6f356afe0738e999f0af2bed27f45), are determined through the use of memory structures. Using these memory structures, the search progresses by iteratively moving from the current solution ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) to an improved solution ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/0ac74959896052e160a5953102e4bc3850fe93b2) in ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/4db1b4a2cfa6f356afe0738e999f0af2bed27f45).

These memory structures form what is known as the tabu list, a set of rules and banned solutions used to filter which solutions will be admitted to the neighborhood ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/4db1b4a2cfa6f356afe0738e999f0af2bed27f45) to be explored by the search. In its simplest form, a tabu list is a short-term set of the solutions that have been visited in the recent past (less than ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/a601995d55609f2d9f5e233e36fbe9ea26011b3b) iterations ago, where ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/a601995d55609f2d9f5e233e36fbe9ea26011b3b) is the number of previous solutions to be stored — is also called the tabu tenure). More commonly, a tabu list consists of solutions that have changed by the process of moving from one solution to another. It is convenient, for ease of description, to understand a “solution” to be coded and represented by such attributes.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Tabu_search)
