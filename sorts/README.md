## Sorting Algorithms

### 0. Selection Sort
![3goa2af](https://user-images.githubusercontent.com/37110949/49509755-982cfc00-f8c9-11e8-83c1-050da5a03e43.png)

From [Wikipedia](https://ko.wikipedia.org/wiki/%EC%84%A0%ED%83%9D_%EC%A0%95%EB%A0%AC): **Selection sort** is an algorithm that divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(n<sup>2</sup>)
* Average case performance	O(n<sup>2</sup>)

###### View the algorithm in [action](https://www.toptal.com/developers/sorting-algorithms/selection-sort)

### 1. Bubble Sort
![bubble-sort-in-c](https://user-images.githubusercontent.com/37110949/49448033-534a8c00-f81b-11e8-8b6a-78c83907ef7d.jpg)

From [Wikipedia][bubble-wiki]: **Bubble sort**, sometimes referred to as *sinking sort*, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent pairs and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(n)
* Average case performance	O(n<sup>2</sup>)

###### View the algorithm in [action](https://www.toptal.com/developers/sorting-algorithms/bubble-sort)

### 2. Insertion Sort
![insertion-sort](https://user-images.githubusercontent.com/37110949/49484510-a99ae780-f87a-11e8-8681-981f5739e03d.png)

From [Wikipedia](https://ko.wikipedia.org/wiki/%EC%82%BD%EC%9E%85_%EC%A0%95%EB%A0%AC): **Insertion sort** is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on *large* lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(n)
* Average case performance	O(n<sup>2</sup>)

###### View the algorithm in [action](https://www.toptal.com/developers/sorting-algorithms/insertion-sort)

### 3. Merge Sort
![how merge sort algorithm works in java](https://user-images.githubusercontent.com/37110949/49570490-19dc6280-f97a-11e8-9d26-10540d5dcd88.png)

From [Wikipedia](https://ko.wikipedia.org/wiki/%ED%95%A9%EB%B3%91_%EC%A0%95%EB%A0%AC): **Merge sort** (also commonly spelled *mergesort*) is an efficient, general-purpose, comparison-based sorting algorithm. Most implementations produce a stable sort, which means the order of equal items is the same in the input and output. Mergesort is a divide and conquer algorithm that was invented by John von Neumann in 1945.

__Properties__
* Worst case performance	O(n log n)
* Best case performance	O(n log n)
* Average case performance	O(n log n)


###### View the algorithm in [action](https://www.toptal.com/developers/sorting-algorithms/merge-sort)

### 4. Tree Sort
![binary-search-tree-insertion-animation](https://user-images.githubusercontent.com/37110949/49629485-1229c600-fa2d-11e8-808a-875b37eba6af.gif)

From [Wikipedia](https://en.wikipedia.org/wiki/Tree_sort): **Tree sort** A tree sort is a sort algorithm that builds a binary search tree from the elements to be sorted, and then traverses the tree (in-order) so that the elements come out in sorted order. Its typical use is sorting elements online: after each insertion, the set of elements seen so far is available in sorted order.
__Properties__
* Worst case performance	O(n<sup>2</sup>)(unblanced), O(n log n)(blanced)
* Best case performance	O(n log n)
* Average case performance	O(n log n)

### 5. Counting Sort
![99279e365ab11c4934](https://user-images.githubusercontent.com/37110949/49685622-bee96d80-fb29-11e8-897f-66d459228ab7.png)


From [Wikipedia](https://en.wikipedia.org/wiki/Counting_sort): **Counting sort** In computer science, counting sort is an algorithm for sorting a collection of objects according to keys that are small integers; that is, it is an integer sorting algorithm. It operates by counting the number of objects that have each distinct key value, and using arithmetic on those counts to determine the positions of each key value in the output sequence. Its running time is linear in the number of items and the difference between the maximum and minimum key values, so it is only suitable for direct use in situations where the variation in keys is not significantly greater than the number of items. However, it is often used as a subroutine in another sorting algorithm, radix sort, that can handle larger keys more efficiently

__Properties__
* Worst case performance, Best case performance	-> O(n+k) depending on k value
* Average case performance	O(n+k)

### 6. Quick Sort
![220px-sorting_quicksort_anim](https://user-images.githubusercontent.com/37110949/49715048-8f09a980-fc92-11e8-8c5b-ffe9aaf51a33.gif)

From [Wikipedia](https://ko.wikipedia.org/wiki/%ED%80%B5_%EC%A0%95%EB%A0%AC): **Quicksort** (sometimes called *partition-exchange sort*) is an efficient sorting algorithm, serving as a systematic method for placing the elements of an array in order.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(*n* log *n*) or O(n) with three-way partition
* Average case performance	O(*n* log *n*)

###### View the algorithm in [action](https://www.toptal.com/developers/sorting-algorithms/quick-sort)

### 7. Heap Sort

From [Wikipedia](https://ko.wikipedia.org/wiki/%ED%9E%99_%EC%A0%95%EB%A0%AC): Heapsort is a comparison-based sorting algorithm. It can be thought of as an improved selection sort. It divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element and moving that to the sorted region

__Properties__
* Worst case performance	O(*n* log *n*)
* Best case performance	O(*n* log *n*)
* Average case performance	O(*n* log *n*)

###### View the algorithm in [action](https://www.toptal.com/developers/sorting-algorithms/heap-sort)

### Bucket Sort
![alt text][bucket-image-1]
![alt text][bucket-image-2]

From [Wikipedia][bucket-wiki]: Bucket sort, or bin sort, is a sorting algorithm that distributes elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(n+k)
* Average case performance	O(n+k)

### Cocktail shaker
![alt text][cocktail-shaker-image]

From [Wikipedia][cocktail-shaker-wiki]: Cocktail shaker sort, also known as bidirectional bubble sort, cocktail sort, shaker sort (which can also refer to a variant of selection sort), ripple sort, shuffle sort, or shuttle sort, is a variation of bubble sort that is both a stable sorting algorithm and a comparison sort. The algorithm differs from a bubble sort in that it sorts in both directions on each pass through the list.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(n)
* Average case performance	O(n<sup>2</sup>)


### Radix

From [Wikipedia][radix-wiki]: Radix sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value.

__Properties__
* Worst case performance	O(wn)
* Best case performance	O(wn)
* Average case performance	O(wn)


### Shell
![alt text][shell-image]

From [Wikipedia][shell-wiki]: **Shellsort** is a generalization of *insertion sort* that allows the exchange of items that are far apart.  The idea is to arrange the list of elements so that, starting anywhere, considering every nth element gives a sorted list.  Such a list is said to be h-sorted.  Equivalently, it can be thought of as h interleaved lists, each individually sorted.

__Properties__
* Worst case performance O(*n*log<sup>2</sup>*n*)
* Best case performance O(*n* log *n*)
* Average case performance depends on gap sequence

###### View the algorithm in [action][shell-toptal]

### Topological

From [Wikipedia][topological-wiki]: A topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. For instance, the vertices of the graph may represent tasks to be performed, and the edges may represent constraints that one task must be performed before another; in this application, a topological ordering is just a valid sequence for the tasks. A topological ordering is possible if and only if the graph has no directed cycles, that is, if it is a directed acyclic graph (DAG). Any DAG has at least one topological ordering, and algorithms are known for constructing a topological ordering of any DAG in linear time.

### Time-Complexity Graphs

Comparing the complexity of sorting algorithms (*Bubble Sort*, *Insertion Sort*, *Selection Sort*)

![Complexity Graphs](https://github.com/prateekiiest/Python/blob/master/sorts/sortinggraphs.png)

Selecting a sort technique: Quicksort is a very fast algorithm but can be pretty tricky to implement while bubble sort is a slow algorithm which is very easy to implement. For a small datasets bubble sort may be a better option since it can be implemented quickly, but for larger datasets, the speedup from quicksort might be worth the trouble implementing the algorithm.


