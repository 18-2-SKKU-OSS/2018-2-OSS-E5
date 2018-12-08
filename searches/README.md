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
 
## 8. 삼분 탐색

**삼분 탐색** 알고리즘은 단측색 함수의 최소 또는 최대값을 찾기 위한 컴퓨터 과학 기술이다. 삼분 탐색은 최소 또는 최대값이 도메인의 첫 번째 3분의 1에 속할 수 없거나 도메인의 마지막 3분의 1에 속할 수 없다고 판단한 다음 남은 리스트에서 이를 반복한다. 3차 검색은 분할 및 정복 알고리즘의 예다.

우리가 최대 f(x)를 찾고 있고 우리가 A와 B 사이의 어딘가에 최대값을 알고 있다고 가정하자. 알고리즘이 적용되려면 다음과 같은 일부 값 x가 있어야 한다.
A ≤ a < b ≤ x, 를 만족하는 모든 a,b에 대해 f(a) < f(b)이고
x ≤ a < b ≤ B,를 만족하는 모든 a,b에 대해 f(a) > f(b) 이다.

 __Properties__
* 평균적인 경우	O(log 3n)

 ###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Ternary_search)
 
