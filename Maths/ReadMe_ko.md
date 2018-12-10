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

__시간 __
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


### Modular exponentiation
![alt text][merge-image]

From [Wikipedia][merge-wiki]: **Modular exponentiation** is a type of exponentiation performed over a modulus. It is useful in computer science, especially in the field of public-key cryptography. The operation of modular exponentiation calculates the remainder when an integer b (the base) raised to the eth power (the exponent), be, is divided by a positive integer m (the modulus). In symbols, given base b, exponent e, and modulus m, the modular exponentiation c is: c = be mod m. From the definition of c, it follows that 0 ≤ c < m. For example, given b = 5, e = 3 and m = 13, the solution c = 8 is the remainder of dividing 53 = 125 by 13.
Modular exponentiation can be performed with a negative exponent e by finding the modular multiplicative inverse d of b modulo m using the extended Euclidean algorithm. That is: c = be mod m = d−e mod m, where e < 0 and b ⋅ d ≡ 1 (mod m). Modular exponentiation similar to the one described above is considered easy to compute, even when the integers involved are enormous. On the other hand, computing the modular discrete logarithm – that is, the task of finding the exponent e when given b, c, and m – is believed to be difficult. This one-way function behavior makes modular exponentiation a candidate for use in cryptographic algorithms.

__Properties__
* Worst case performance	O(M(n) k))
* Best case performance	O(M(n) k)
* Average case performance	O(M(n) k)


### Tower of Hanoi
![alt text][quick-image]

From [Wikipedia][quick-wiki]: **The Tower of Hanoi**(also called the Tower of Brahma or Lucas' Tower and sometimes pluralized) is a mathematical game or puzzle. It consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.
The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
>1. Only one disk can be moved at a time.
>2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
>3. No larger disk may be placed on top of a smaller disk.
With 3 disks, the puzzle can be solved in 7 moves. The minimal number of moves required to solve a Tower of Hanoi puzzle is 2n − 1, where n is the number of disks.

__Properties__
* Worst case performance	O(2<sup>n</sup>)
* Best case performance O(2<sup>n</sup>)
* Average case performance	O(2<sup>n</sup>)



### Simpson's Rule
![alt text][simpson-rule]

From [Wikipedia](https://en.wikipedia.org/wiki/Simpson%27s_rule): In numerical analysis, **Simpson's rule** is a method for numerical integration, the numerical approximation of definite integrals. Specifically, it is the following approximation for n equally spaced subdivisions (where n is even): (General Form)

__Properties__
* Worst case performance	O(n)
* Best case performance	O(n)
* Average case performance	O(n)

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
