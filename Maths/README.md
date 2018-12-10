# Maths - Python <!-- [![Build Status](https://travis-ci.org/TheAlgorithms/Python.svg)](https://travis-ci.org/TheAlgorithms/Python) -->

### All Math algorithms implemented in Python (for education)

These implementations are for demonstration purposes. They are less efficient than the implementations in the Python standard library.

## Math Algorithms


### Factorial
![number-factorial-calculation](https://user-images.githubusercontent.com/37097363/49742832-bdac7200-fcdc-11e8-92c8-3f368761127b.jpg)

From [Wikipedia][bubble-wiki]: **Factorial**, In mathematics, the factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n. The factorial operation is encountered in many areas of mathematics, notably in combinatorics, algebra, and mathematical analysis. Its most basic occurrence is the fact that there are n! ways to arrange n distinct objects into a sequence. These arrangements are called the permutations of the set of objects. The definition of the factorial function can also be extended to non-integer arguments, while retaining its most important properties; this involves more advanced mathematics, notably techniques from mathematical analysis.

__Properties__
* Worst case performance	On)
* Best case performance	O(n)
* Average case performance	O(n)


### Fibonacci Sequence
![alt text][bucket-image-1]

From [Wikipedia][bucket-wiki]: In mathematics, the Fibonacci numbers, commonly denoted Fn form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.

__Properties__
* Worst case performance	O(2<sup>n</sup>)
* Best case performance O(2<sup>n</sup>)
* Average case performance	O(2<sup>n</sup>)

### Find Highest Common Factor
![alt text][cocktail-shaker-image]

From [Wikipedia][cocktail-shaker-wiki]: In mathematics, the greatest common divisor (gcd) of two or more integers, which are not all zero, is the largest positive integer that divides each of the integers. For example, the gcd of 8 and 12 is 4. This notion can be extended to polynomials (see Polynomial greatest common divisor) and other commutative rings.

__Properties__
* Worst case performance	O(log n)
* Best case performance	O(log n)
* Average case performance	O(log n)


### Find Least Common Multiple
![alt text][insertion-image]

From [Wikipedia][insertion-wiki]: In arithmetic and number theory, **Least common multiple**, lowest common multiple, or smallest common multiple of two integers a and b, usually denoted by LCM(a, b), is the smallest positive integer that is divisible by both a and b.[1] Since division of integers by zero is undefined, this definition has meaning only if a and b are both different from zero.[2] However, some authors define LCM (a,0) as 0 for all a, which is the result of taking the LCM to be the least upper bound in the lattice of divisibility. The LCM is the "lowest common denominator" (LCD) that can be used before fractions can be added, subtracted or compared. The LCM of more than two integers is also well-defined: it is the smallest positive integer that is divisible by each of them.

__Properties__
* Worst case performance	O(n)
* Best case performance	O(n)
* Average case performance	O(n)


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
