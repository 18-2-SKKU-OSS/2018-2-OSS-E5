## Search Algorithms

### 1. Linear Search
![1 linear_search](https://user-images.githubusercontent.com/38908132/49446326-4cba1580-f817-11e8-9397-102eebbdfb0e.gif)

**Linear search** or *sequential search* is a method for finding an element in a list. It sequentially checks each element of the list until a match is found or all the elements have been searched.

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Linear_search)
__Properties__
* Worst case performance	O(n)
* Best case performance	O(1)
* Average case performance	O(n)
* Worst case space complexity	O(1) iterative

### 2. Binary Search
![2 binary_search](https://user-images.githubusercontent.com/38908132/49446327-4cba1580-f817-11e8-8efa-032610735e42.png)

**Binary search**, also known as *half-interval search* or *logarithmic search*, is a search algorithm that finds the position of a target value within a sorted array. It compares the target value to the middle element of the array; if they are unequal, the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful.

__Properties__
* Worst case performance	O(log n)
* Best case performance	O(1)
* Average case performance	O(log n)
* Worst case space complexity	O(1)

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)

## 3. Interpolation Search
**Interpolation search** is an algorithm for searching for a key in an array that has been ordered by numerical values assigned to the keys (key values). It was first described by W. W. Peterson in 1957. Interpolation search resembles the method by which people search a telephone directory for a name (the key value by which the book's entries are ordered): in each step the algorithm calculates where in the remaining search space the sought item might be, based on the key values at the bounds of the search space and the value of the sought key, usually via a linear interpolation. The key value actually found at this estimated position is then compared to the key value being sought. If it is not equal, then depending on the comparison, the remaining search space is reduced to the part before or after the estimated position. This method will only work if calculations on the size of differences between key values are sensible.

By comparison, binary search always chooses the middle of the remaining search space, discarding one half or the other, depending on the comparison between the key found at the estimated position and the key sought — it does not require numerical values for the keys, just a total order on them. The remaining search space is reduced to the part before or after the estimated position. The linear search uses equality only as it compares elements one-by-one from the start, ignoring any sorting.

__Properties__
* Worst case performance	O(n)
* Average case performance	O(log log n)

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Interpolation_search)

## 4. Jump Search
![4 jump_search](https://user-images.githubusercontent.com/38908132/49446328-4d52ac00-f817-11e8-9a61-09da54796142.jpg)

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
![5 quick_search](https://user-images.githubusercontent.com/38908132/49446329-4d52ac00-f817-11e8-8cb8-64c716fc6732.gif)

**Quickselect** is a selection algorithm to find the kth smallest element in an unordered list. It is related to the quicksort sorting algorithm. Like quicksort, it was developed by Tony Hoare, and thus is also known as Hoare's selection algorithm. Like quicksort, it is efficient in practice and has good average-case performance, but has poor worst-case performance. Quickselect and its variants are the selection algorithms most often used in efficient real-world implementations.

Quickselect uses the same overall approach as quicksort, choosing one element as a pivot and partitioning the data in two based on the pivot, accordingly as less than or greater than the pivot. However, instead of recursing into both sides, as in quicksort, quickselect only recurses into one side – the side with the element it is searching for. This reduces the average complexity from O(n log n) to O(n), with a worst case of O(n<sup>2</sup>).

As with quicksort, quickselect is generally implemented as an in-place algorithm, and beyond selecting the k'th element, it also partially sorts the data. See selection algorithm for further discussion of the connection with sorting.

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Quickselect)

## 6. Fibonacci Search
![fibsearch31-660x578](https://user-images.githubusercontent.com/38908132/49605746-b7648000-f9d4-11e8-8d08-6879863aa30b.png)

**Fibonacci search** technique is a method of searching a sorted array using a divide and conquer algorithm that narrows down possible locations with the aid of Fibonacci numbers.[1] Compared to binary search where the sorted array is divided into two equal-sized parts, one of which is examined further, Fibonacci search divides the array into two parts that have sizes that are consecutive Fibonacci numbers.

Fibonacci Numbers are recursively defined as F(n) = F(n-1) + F(n-2), F(0) = 0, F(1) = 1. First few Fibinacci Numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

__Properties__
* Worst case performance	O(log n)
* Average case performance	O(log n)\

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_search_technique)

## 7. Exponential Search

**exponential search** (also called doubling search or galloping search or Struzik search) is an algorithm, created by Jon Bentley and Andrew Chi-Chih Yao in 1976, for searching sorted, unbounded/infinite lists. There are numerous ways to implement this with the most common being to determine a range that the search key resides in and performing a binary search within that range. 

The idea is to start with subarray size 1, compare its last element with x, then try size 2, then 4 and so on until last element of a subarray is not greater. Once we find an index i (after repeated doubling of i), we know that the element must be present between i/2 and i (Why i/2? because we could not find a greater value in previous iteration)

__Properties__
* Worst case performance	O(log n)
* Average case performance	O(log n)

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Exponential_search)

## 8. Tabu Search
Tabu search uses a local or neighborhood search procedure to iteratively move from one potential solution ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) to an improved solution ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/0ac74959896052e160a5953102e4bc3850fe93b2) in the neighborhood of ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4), until some stopping criterion has been satisfied (generally, an attempt limit or a score threshold). Local search procedures often become stuck in poor-scoring areas or areas where scores plateau. In order to avoid these pitfalls and explore regions of the search space that would be left unexplored by other local search procedures, tabu search carefully explores the neighborhood of each solution as the search progresses. The solutions admitted to the new neighborhood, ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/4db1b4a2cfa6f356afe0738e999f0af2bed27f45), are determined through the use of memory structures. Using these memory structures, the search progresses by iteratively moving from the current solution ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) to an improved solution ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/0ac74959896052e160a5953102e4bc3850fe93b2) in ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/4db1b4a2cfa6f356afe0738e999f0af2bed27f45).

These memory structures form what is known as the tabu list, a set of rules and banned solutions used to filter which solutions will be admitted to the neighborhood ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/4db1b4a2cfa6f356afe0738e999f0af2bed27f45) to be explored by the search. In its simplest form, a tabu list is a short-term set of the solutions that have been visited in the recent past (less than ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/a601995d55609f2d9f5e233e36fbe9ea26011b3b) iterations ago, where ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/a601995d55609f2d9f5e233e36fbe9ea26011b3b) is the number of previous solutions to be stored — is also called the tabu tenure). More commonly, a tabu list consists of solutions that have changed by the process of moving from one solution to another. It is convenient, for ease of description, to understand a “solution” to be coded and represented by such attributes.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Tabu_search)
