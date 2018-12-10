## Math Algorithms


### 팩토리얼
![number-factorial-calculation](https://user-images.githubusercontent.com/37097363/49742832-bdac7200-fcdc-11e8-92c8-3f368761127b.jpg)

From [Wikipedia][bubble-wiki]: **Factorial**, 수학에서, 자연수의 계승(階乘, 문화어: 차례곱, 영어: factorial 팩토리얼)은 그 수보다 작거나 같은 모든 양의 정수의 곱이다. n이 하나의 자연수일 때, 1에서 n까지의 모든 자연수의 곱을 n에 상대하여 이르는 말이다. 기호는 을 쓰며 팩토리얼이라고 읽는다.

__시간 복잡도__
* 최악의 경우	O(n)
* 최선의 경우	O(n)
* 평균의 경우	O(n)


### 피보나치 수열
![alt text][bucket-image-1]

From [Wikipedia][bucket-wiki]: 수학에서, 피보나치 수(영어: Fibonacci numbers)는 첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열이다. 처음 여섯 항은 각각 1, 1, 2, 3, 5, 8이다. 편의상 0번째 항을 0으로 두기도 한다.

__시간 복잡도__
* 최악의 경우	O(2<sup>n</sup>)
* 최선의 경우 O(2<sup>n</sup>)
* 평균의 경우	O(2<sup>n</sup>)

### 최대공약수 찾기
![alt text][cocktail-shaker-image]

From [Wikipedia][cocktail-shaker-wiki]: 수론에서, 정수들의 공약수(公約數, 영어: common divisor)는 동시에 그들 모두의 약수인 정수다. 적어도 하나가 0이 아닌 정수들의 최대공약수(最大公約數, 문화어: 련속나눔셈; 영어: greatest common divisor, 약자 GCD)는 공약수 가운데 가장 큰 하나다. 다항식이나 환의 원소에 대해서도 정의할 수 있다.

__시간 복잡도__
* 최악의 경우	O(log n)
* 최선의 경우	O(log n)
* 평균의 경우	O(log n)


### 최소공배수 찾기
![alt text][insertion-image]

From [Wikipedia][insertion-wiki]: 수론에서, 여러 개의 정수/다항식/환의 원소의 공배수(公倍數, 영어: common multiple)는 그들 모두의 배수가 되는 정수/다항식/환의 원소이다. 최소공배수(最小公倍數, 영어: least common multiple/ lowest common multiple, 약자 LCM)는 양의 공배수 가운데 가장 작은 하나이다. 유클리드 정역에서 0으로 나누기를 정의하지 않으므로, 이 정의는 오직 다루고자 하는 정수들이 0이 아닐 때 의미가 있다. 그러나 일부 저자는 {\displaystyle \operatorname {lcm} \{a,0\}} {\displaystyle \operatorname {lcm} \{a,0\}}을 모든 a에 대해 0으로 정의하며, 이는 나눗셈의 격자에서 최소공배수를 최소 상한으로 간주한 것이다.

__시간 복잡도__
* 최악의 경우	O(n)
* 최선의 경우	O(n)
* 평균의 경우	O(n)


### 모듈러 거듭제곱
![alt text][merge-image]

From [Wikipedia][merge-wiki]: **모듈러 거듭제곱**는 계수 위에 수행되는 성분의 한 유형이다. 그것은 컴퓨터 과학, 특히 공중키 암호학 분야에서 유용하다. 모듈형 지수의 운영은 윤리력(지수)으로 상승한 정수 b가 양의 정수 m(계수)로 분할될 때 나머지를 계산한다. 기호, 주어진 b, 지수 e 및 계수 m에서 모듈식 지수 c는 다음과 같다. c = mod m. c의 정의에서 0 ≤ c < m. 예를 들어, b = 5, e = 3 및 m = 13이 주어진 경우, 솔루션 c = 8은 53 = 125를 13으로 나눈 나머지 값이다.
모듈 형성은 확장 유클리드 알고리즘을 사용해 b modulo m의 모듈형 곱셈 역 d를 찾아 음수 지수 e로 수행할 수 있다. 즉, c = mod m = d-e m, 여기서 e < 0 및 b ⋅ d ≡ 1 (mod m)이다. 위에 설명한 것과 유사한 모듈식 표현은 관련된 정수가 엄청나더라도 계산하기 쉬운 것으로 간주된다. 반면에 모듈식 이산 로그(즉, b, c, m)를 계산할 때 지수 e를 찾는 일은 어려운 것으로 간주된다. 이러한 단방향 기능 행동은 모듈식 설명을 암호화 알고리즘에 사용할 수 있는 후보로 만든다.

__시간 복잡도__
* 최악의 경우	O(M(n) k))
* 최선의 경우	O(M(n) k)
* 평균의 경우 	O(M(n) k)


### 하노이의 탑
![alt text][quick-image]

From [Wikipedia][quick-wiki]: **하노이의 탑**(Tower of Hanoi)은 퍼즐의 일종이다. 세 개의 기둥과 이 기둥에 꽂을 수 있는 크기가 다양한 원판들이 있고, 퍼즐을 시작하기 전에는 한 기둥에 원판들이 작은 것이 위에 있도록 순서대로 쌓여 있다. 게임의 목적은 다음 두 가지 조건을 만족시키면서, 한 기둥에 꽂힌 원판들을 그 순서 그대로 다른 기둥으로 옮겨서 다시 쌓는 것이다.

>1. 한 번에 하나의 원판만 옮길 수 있다.
>2. 큰 원판이 작은 원판 위에 있어서는 안 된다.

하노이의 탑 문제는 재귀 호출을 이용하여 풀 수 있는 가장 유명한 예제 중의 하나이다. 그렇기 때문에 프로그래밍 수업에서 알고리즘 예제로 많이 사용한다. 일반적으로 원판이 n개 일 때, 2n -1번의 이동으로 원판을 모두 옮길 수 있다(2n − 1는 메르센 수라고 부른다). 참고로 64개의 원판을 옮기는 데 약 18446744073709551615번을 움직여야 하고, 한번 옮길 때 시간을 1초로 가정했을 때 64개의 원판을 옮기는 데 5849억 4241만 7355년이 걸린다.

__시간 복잡도__
* 최악의 경우	O(2<sup>n</sup>)
* 최선의 경우  O(2<sup>n</sup>)
* 평균의 경우	O(2<sup>n</sup>)



### 심프슨 공식
![alt text][simpson-rule]

From [Wikipedia](https://en.wikipedia.org/wiki/Simpson%27s_rule): **심프슨 공식**(영어: Simpson's rule)은 수치 해석에서 뉴턴-코츠 법칙의 한 경우로, 토머스 심프슨이 만든 적분법이다. 이 법칙은 다음과 같은 적분식의 근사값을 구하는 데 쓰인다.

__시간 복잡도__
* 최악의 경우	O(n)
* 최선의 경우	O(n)
* 평균의 경우	O(n)

[bubble-toptal]: https://www.toptal.com/developers/sorting-algorithms/bubble-sort
[bubble-wiki]: https://en.wikipedia.org/wiki/Factorial
[bubble-image]: https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Bubblesort-edited-color.svg/220px-Bubblesort-edited-color.svg.png "Bubble Sort"

[bucket-wiki]: https://en.wikipedia.org/wiki/Fibonacci_number
[bucket-image-1]: https://upload.wikimedia.org/wikipedia/commons/d/db/34%2A21-FibonacciBlocks.png
[bucket-image-2]: https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Bucket_sort_2.svg/311px-Bucket_sort_2.svg.png "Bucket Sort"

[cocktail-shaker-wiki]: https://en.wikipedia.org/wiki/Greatest_common_divisor
[cocktail-shaker-image]: https://image.slidesharecdn.com/saikat-20roy-20-20me-20software-20engg-20-2026-140402183023-phpapp02/95/gcd-of-n-numbers-3-638.jpg?cb=1396463613

[insertion-toptal]: https://www.toptal.com/developers/sorting-algorithms/insertion-sort
[insertion-wiki]: https://en.wikipedia.org/wiki/Least_common_multiple
[insertion-image]: https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Least_common_multiple_chart.png/375px-Least_common_multiple_chart.png

[quick-toptal]: https://www.toptal.com/developers/sorting-algorithms/quick-sort
[quick-wiki]: https://en.wikipedia.org/wiki/Tower_of_Hanoi
[quick-image]: https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Tower_of_Hanoi.jpeg/450px-Tower_of_Hanoi.jpeg

[radix-wiki]: https://en.wikipedia.org/wiki/Radix_sort

[merge-toptal]: https://www.toptal.com/developers/sorting-algorithms/merge-sort
[merge-wiki]: https://en.wikipedia.org/wiki/Modular_exponentiation
[merge-image]: https://i.stack.imgur.com/L5W3I.png

[simpson-rule]: https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Simpsons_method_illustration.svg/330px-Simpsons_method_illustration.svg.png
