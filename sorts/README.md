# The Algorithms - Python <!-- [![Build Status](https://travis-ci.org/TheAlgorithms/Python.svg)](https://travis-ci.org/TheAlgorithms/Python) -->

### All algorithms implemented in Python (for education)

These implementations are for demonstration purposes. They are less efficient than the implementations in the Python standard library.

## Sorting Algorithms


### Bubble Sort
![alt text][bubble-image]

From [Wikipedia][bubble-wiki]: **Bubble sort**, sometimes referred to as *sinking sort*, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent pairs and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(n)
* Average case performance	O(n<sup>2</sup>)

###### View the algorithm in [action][bubble-toptal]

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


### Insertion Sort
![alt text][insertion-image]

From [Wikipedia][insertion-wiki]: **Insertion sort** is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on *large* lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(n)
* Average case performance	O(n<sup>2</sup>)

###### View the algorithm in [action][insertion-toptal]


### Merge Sort
![alt text][merge-image]

From [Wikipedia][merge-wiki]: **Merge sort** (also commonly spelled *mergesort*) is an efficient, general-purpose, comparison-based sorting algorithm. Most implementations produce a stable sort, which means the order of equal items is the same in the input and output. Mergesort is a divide and conquer algorithm that was invented by John von Neumann in 1945.

__Properties__
* Worst case performance	O(n log n)
* Best case performance	O(n log n)
* Average case performance	O(n log n)


###### View the algorithm in [action][merge-toptal]

### Quick Sort
![alt text][quick-image]

From [Wikipedia][quick-wiki]: **Quicksort** (sometimes called *partition-exchange sort*) is an efficient sorting algorithm, serving as a systematic method for placing the elements of an array in order.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(*n* log *n*) or O(n) with three-way partition
* Average case performance	O(*n* log *n*)

###### View the algorithm in [action][quick-toptal]


### Heap

From [Wikipedia](https://en.wikipedia.org/wiki/Heapsort): Heapsort is a comparison-based sorting algorithm. It can be thought of as an improved selection sort. It divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element and moving that to the sorted region

__Properties__
* Worst case performance	O(*n* log *n*)
* Best case performance	O(*n* log *n*)
* Average case performance	O(*n* log *n*)



###### View the algorithm in [action](https://www.toptal.com/developers/sorting-algorithms/heap-sort)

### Radix

From [Wikipedia][radix-wiki]: Radix sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value.

__Properties__
* Worst case performance	O(wn)
* Best case performance	O(wn)
* Average case performance	O(wn)

### Selection
![alt text][selection-image]

From [Wikipedia][selection-wiki]: **Selection sort** is an algorithm that divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(n<sup>2</sup>)
* Average case performance	O(n<sup>2</sup>)

###### View the algorithm in [action][selection-toptal]

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


