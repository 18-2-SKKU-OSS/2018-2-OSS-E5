## 탐색 알고리즘

### 1. 선형 탐색
![1 linear_search](https://user-images.githubusercontent.com/38908132/49684284-54c6cd80-fb15-11e8-946a-290519ac5588.gif)

**선형 탐색** 또는 순차 탐색은 목록 내의 대상을 찾는 방법입니다. 찾는 값과 요소의 값이 일치하거나 모든 요소가 검색 될 때까지 목록의 요소 값에 대해 순차적으로 탐색합니다. 선형 검색은 최악의 시간복잡도 내에서 움직이며 최대 n 개의 비교를 수행합니다. 여기서 n은 목록의 길이입니다.

__Properties__
* 최악의 경우	O(n)
* 최선의 경우	O(1)
* 평균적인 경우	O(n)

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Linear_search)

### 2. 이진 탐색
![2 binary_search](https://user-images.githubusercontent.com/38908132/49684281-54c6cd80-fb15-11e8-8d9a-d3928cea5afa.png)

**이진 탐색**은 반 간격 검색 또는 로그 검색이라고도 하는 이진 검색은 정렬된 배열 내에서 대상 값의 위치를 찾는 탐색 알고리즘입니다. 목표 값을 배열의 중간 요소와 비교하여 동일하지 않으면, 절반을 배제한 상태로 다시 성공할 때까지 나머지 절반의 탐색을 진행합니다.

__Properties__
* 최악의 경우	O(log n)
* 최선의 경우	O(1)
* 평균적인 경우	O(log n)

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)

## 3. 보간 탐색

**보간 탐색**는 배열에서 키에 할당된 숫자 값(키 값)으로 정렬된 키를 검색하는 알고리즘이다. 이 알고리즘은 1957년에 W. W. Peterson에 의해 처음 묘사되었다. 보간 탐색은 사람들이 전화 디렉토리에서 이름을 검색하는 방법(책의 항목을 정렬하는 키 값)과 유사하다: 각 단계에서 알고리즘은 검색 공간의 경계에 있는 키 값과 원하는 키의 값에 기초하여 검색된 항목이 있을 수 있는 나머지 검색 공간의 위치를 선형 보간법을 통해 계산한다. 이 추정된 위치에서 실제로 발견된 키 값을 찾고 있는 키 값과 비교한다. 동일하지 않으면 비교에 따라 나머지 검색 공간은 추정 위치 이전 또는 이후 부품으로 축소된다. 이 방법은 키 값 사이의 차이 크기에 대한 계산이 합리적인 경우에만 작동한다.

이에 비해 이진 탐색은 항상 남은 검색 공간의 중간을 선택하고, 추정된 위치에서 찾은 키와 탐색한 키 간의 비교에 따라 한 쪽 또는 다른 쪽 검색 공간을 버린다. 키에 대한 숫자 값은 필요 없고, 전체 순서만 필요하다. 나머지 검색 공간은 추정 위치 이전 또는 이후 부품으로 축소된다. 선형 탐색은 정렬을 무시하면서 시작부터 요소를 하나씩 비교하는 경우에만 평등을 사용한다.

__Properties__
* 최악의 경우	O(n)
* 평균적인 경우	O(log log n)

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Interpolation_search)

## 4. 점프 탐색
![4 jump_search](https://user-images.githubusercontent.com/38908132/49684282-54c6cd80-fb15-11e8-98b3-e3a9108ddf83.jpg)

**점프 탐색** 또는 블록 탐색은 정렬된 리스트에 대한 검색 알고리즘이다. 검색 키보다 큰 항목이 발견될 때까지 모든 L<sub>km</sub>항목을 확인한다. (m은 블록 사이즈) 목록에서 검색 키의 정확한 위치를 찾기 위해 하위 목록 L<sub>[(k-1)m, km]</sub>.에서는 선형 탐색이 수행된다.

__Properties__
* 최악의 경우	O(sqrt n)
* 최선의 경우	O(1)
* 평균적인 경우	O(sqrt n)

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Jump_search)

## 5. 퀵 셀렉트 탐색
![5 quick_search](https://user-images.githubusercontent.com/38908132/49684283-54c6cd80-fb15-11e8-802f-257c4f85c5fb.gif)

**퀵 셀렉트 탐색**은 정렬되지 않은 목록에서 k번째 가장 작은 요소를 찾는 선택 알고리즘이다. 이것은 퀵소트 정렬 알고리즘과 관련이 있다. Tony Hoare에 의해 개발되었으며 Hoare의 선택 알고리즘으로도 알려져 있다. 퀵소트처럼 평균적인 성능은 좋지만, 최악의 경우에는 성능이 매우 나쁘다. 퀵 셀렉트 탐색과 그것의 변형은 실제 세계에서 자주 사용되는 선택 알고리즘이다.

__Properties__
* 최악의 경우 O(n)
* 평균적인 경우	O(log n)

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Quickselect)

## 6. 피보나치 탐색
![fibsearch31-660x578](https://user-images.githubusercontent.com/38908132/49605746-b7648000-f9d4-11e8-8d08-6879863aa30b.png)
 
 **피보나치 탐색** 은 피보나치 수열을 이용하여 가능한 위치를 좁히는 분할 및 정복 알고리즘을 사용하여 정렬된 배열을 검색하는 방법이다. 이진 탐색의 경우 정렬된 배열을 동일한 크기의 두 부분으로 나누는 반면, 피보나치 탐색은 배열을 연속적인 피보나치 수만큼의 두 부분으로 나눈다.

__Properties__
* 최악의 경우	O(log n)
* 평균적인 경우 O(log n)

 ###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_search_technique)
 
## 7. 지수 탐색

**피보나치 탐색**은 정렬되 있고 바인딩되지 않은/무한 목록을 검색하기 위해 1976년 존 벤틀리와 앤드류 치치 야오가 고안한 알고리즘이다. 검색 키가 있는 범위를 결정하고 해당 범위 내에서 이진 검색을 수행하는 것이 가장 일반적인 방법이며 이것을 구현하는 방법은 다양하다. 
아이디어는 부분 리스트의 크기를 1로 시작하고 마지막 요소를 x와 비교한 후 부분 리스트의 마지막 요소가 더 크지 않을 때까지 사이즈 2를 시도해 보는 것이다. 색인 i를 찾으면, 우리가 찾으려고 하는 값이 i/2와 i 사이에 있어야 한다는 것을 알 수 있다.
 
 __Properties__
* 최악의 경우	O(log n)
* 평균적인 경우	O(log n)

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
