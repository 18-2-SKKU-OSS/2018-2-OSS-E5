
# E5 팀원 소개
### 김우경
* Mail: mj9926@naver.com
* ID: kwk2696
* SID: 2017312637
* Role: 팀장, 위키관리, Machine Learning
***
### 박관종
* Mail: dbfltkfkd01@naver.com
* ID: parkgwanjong
* SID: 2017312108
* Role: Machine Learning
***
### 서성윤
* Mail: rudobco0825@gmail.com
* ID: Pleiadex
* SID: 2017310794
* Role: Math
***
### 오승진
* Mail: oiu7934@naver.com
* ID: OhSeungJin
* SID: 2017314628
* Role: Data Structure 
***
### 허종원
* Mail: whddnjs588@naver.com
* ID: HeoJongWon
* SID: 2017313150
* Role: Sorting Algorithms
***
* Project URL: https://github.com/TheAlgorithms/Python
* Group Activites: https://github.com/18-2-SKKU-OSS/2018-2-OSS-E5/wiki/Activites
* Group Docs: https://drive.google.com/open?id=15VQQI6trnJVe29v_ixXwmIa30OwJnN0j




----------------------------------------------------------------------------------

## Search Algorithms

### Linear
![alt text][linear-image]

From [Wikipedia][linear-wiki]: **Linear search** or *sequential search* is a method for finding an element in a list. It sequentially checks each element of the list until a match is found or all the elements have been searched.

__Properties__
* Worst case performance	O(n)
* Best case performance	O(1)
* Average case performance	O(n)
* Worst case space complexity	O(1) iterative

### Binary
![alt text][binary-image]

From [Wikipedia][binary-wiki]: **Binary search**, also known as *half-interval search* or *logarithmic search*, is a search algorithm that finds the position of a target value within a sorted array. It compares the target value to the middle element of the array; if they are unequal, the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful.

__Properties__
* Worst case performance	O(log n)
* Best case performance	O(1)
* Average case performance	O(log n)
* Worst case space complexity	O(1)

## Interpolation
Interpolation search is an algorithm for searching for a key in an array that has been ordered by numerical values assigned to the keys (key values). It was first described by W. W. Peterson in 1957. Interpolation search resembles the method by which people search a telephone directory for a name (the key value by which the book's entries are ordered): in each step the algorithm calculates where in the remaining search space the sought item might be, based on the key values at the bounds of the search space and the value of the sought key, usually via a linear interpolation. The key value actually found at this estimated position is then compared to the key value being sought. If it is not equal, then depending on the comparison, the remaining search space is reduced to the part before or after the estimated position. This method will only work if calculations on the size of differences between key values are sensible.

By comparison, binary search always chooses the middle of the remaining search space, discarding one half or the other, depending on the comparison between the key found at the estimated position and the key sought — it does not require numerical values for the keys, just a total order on them. The remaining search space is reduced to the part before or after the estimated position. The linear search uses equality only as it compares elements one-by-one from the start, ignoring any sorting.

On average the interpolation search makes about log(log(n)) comparisons (if the elements are uniformly distributed), where n is the number of elements to be searched. In the worst case (for instance where the numerical values of the keys increase exponentially) it can make up to O(n) comparisons.

In interpolation-sequential search, interpolation is used to find an item near the one being searched for, then linear search is used to find the exact item.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Interpolation_search)

## Jump Search
![alt text][JumpSearch-image]
In computer science, a jump search or block search refers to a search algorithm for ordered lists. It works by first checking all items L<sub>km</sub>, where ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/2a5bc4b7383031ba693b7433198ead7170954c1d)  and *m* is the block size, until an item is found that is larger than the search key. To find the exact position of the search key in the list a linear search is performed on the sublist L<sub>[(k-1)m, km]</sub>.

The optimal value of m is √n, where n is the length of the list L. Because both steps of the algorithm look at, at most, √n items the algorithm runs in O(√n) time. This is better than a linear search, but worse than a binary search. The advantage over the latter is that a jump search only needs to jump backwards once, while a binary can jump backwards up to log n times. This can be important if a jumping backwards takes significantly more time than jumping forward.

The algorithm can be modified by performing multiple levels of jump search on the sublists, before finally performing the linear search. For an k-level jump search the optimum block size m<sub>l</sub> for the l<sup>th</sup> level (counting from 1) is n<sup>(k-l)/k</sup>. The modified algorithm will perform *k* backward jumps and runs in O(kn<sup>1/(k+1)</sup>) time.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Jump_search)

## Quick Select
![alt text][QuickSelect-image]
In computer science, quickselect is a selection algorithm to find the kth smallest element in an unordered list. It is related to the quicksort sorting algorithm. Like quicksort, it was developed by Tony Hoare, and thus is also known as Hoare's selection algorithm. Like quicksort, it is efficient in practice and has good average-case performance, but has poor worst-case performance. Quickselect and its variants are the selection algorithms most often used in efficient real-world implementations.

Quickselect uses the same overall approach as quicksort, choosing one element as a pivot and partitioning the data in two based on the pivot, accordingly as less than or greater than the pivot. However, instead of recursing into both sides, as in quicksort, quickselect only recurses into one side – the side with the element it is searching for. This reduces the average complexity from O(n log n) to O(n), with a worst case of O(n<sup>2</sup>).

As with quicksort, quickselect is generally implemented as an in-place algorithm, and beyond selecting the k'th element, it also partially sorts the data. See selection algorithm for further discussion of the connection with sorting.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Quickselect)

## Tabu
Tabu search uses a local or neighborhood search procedure to iteratively move from one potential solution ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) to an improved solution ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/0ac74959896052e160a5953102e4bc3850fe93b2) in the neighborhood of ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4), until some stopping criterion has been satisfied (generally, an attempt limit or a score threshold). Local search procedures often become stuck in poor-scoring areas or areas where scores plateau. In order to avoid these pitfalls and explore regions of the search space that would be left unexplored by other local search procedures, tabu search carefully explores the neighborhood of each solution as the search progresses. The solutions admitted to the new neighborhood, ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/4db1b4a2cfa6f356afe0738e999f0af2bed27f45), are determined through the use of memory structures. Using these memory structures, the search progresses by iteratively moving from the current solution ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) to an improved solution ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/0ac74959896052e160a5953102e4bc3850fe93b2) in ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/4db1b4a2cfa6f356afe0738e999f0af2bed27f45).

These memory structures form what is known as the tabu list, a set of rules and banned solutions used to filter which solutions will be admitted to the neighborhood ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/4db1b4a2cfa6f356afe0738e999f0af2bed27f45) to be explored by the search. In its simplest form, a tabu list is a short-term set of the solutions that have been visited in the recent past (less than ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/a601995d55609f2d9f5e233e36fbe9ea26011b3b) iterations ago, where ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/a601995d55609f2d9f5e233e36fbe9ea26011b3b) is the number of previous solutions to be stored — is also called the tabu tenure). More commonly, a tabu list consists of solutions that have changed by the process of moving from one solution to another. It is convenient, for ease of description, to understand a “solution” to be coded and represented by such attributes.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Tabu_search)
----------------------------------------------------------------------------------------------------------------------

## Ciphers

### Caesar
![alt text][caesar]<br>
**Caesar cipher**, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.<br>
It is **a type of substitution cipher** in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. <br>
The method is named after **Julius Caesar**, who used it in his private correspondence.<br>
The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in modern practice offers essentially no communication security.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)

### Vigenère
The **Vigenère cipher** is a method of encrypting alphabetic text by using a series of **interwoven Caesar ciphers** based on the letters of a keyword. It is **a form of polyalphabetic substitution**.<br>
The Vigenère cipher has been reinvented many times. The method was originally described by Giovan Battista Bellaso in his 1553 book La cifra del. Sig. Giovan Battista Bellaso; however, the scheme was later misattributed to Blaise de Vigenère in the 19th century, and is now widely known as the "Vigenère cipher".<br>
Though the cipher is easy to understand and implement, for three centuries it resisted all attempts to break it; this earned it the description **le chiffre indéchiffrable**(French for 'the indecipherable cipher').
Many people have tried to implement encryption schemes that are essentially Vigenère ciphers. Friedrich Kasiski was the first to publish a general method of deciphering a Vigenère cipher in 1863.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

### Transposition

In cryptography, a **transposition cipher** is a method of encryption by which the positions held by units of plaintext (which are commonly characters or groups of characters) are shifted according to a regular system, so that the ciphertext constitutes a permutation of the plaintext. That is, the order of the units is changed (the plaintext is reordered).<br>

Mathematically a bijective function is used on the characters' positions to encrypt and an inverse function to decrypt.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Transposition_cipher)

### RSA (Rivest–Shamir–Adleman)
RSA (Rivest–Shamir–Adleman) is one of the first public-key cryptosystems and is widely used for secure data transmission. In such a cryptosystem, the encryption key is public and it is different from the decryption key which is kept secret (private). In RSA, this asymmetry is based on the practical difficulty of the factorization of the product of two large prime numbers, the "factoring problem". The acronym RSA is made of the initial letters of the surnames of Ron Rivest, Adi Shamir, and Leonard Adleman, who first publicly described the algorithm in 1978. Clifford Cocks, an English mathematician working for the British intelligence agency Government Communications Headquarters (GCHQ), had developed an equivalent system in 1973, but this was not declassified until 1997.

A user of RSA creates and then publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers must be kept secret. Anyone can use the public key to encrypt a message, but with currently published methods, and if the public key is large enough, only someone with knowledge of the prime numbers can decode the message feasibly. Breaking RSA encryption is known as the RSA problem. Whether it is as difficult as the factoring problem remains an open question.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

## ROT13
![alt text][ROT13-image]
ROT13 ("rotate by 13 places", sometimes hyphenated ROT-13) is a simple letter substitution cipher that replaces a letter with the 13th letter after it, in the alphabet. ROT13 is a special case of the Caesar cipher which was developed in ancient Rome.

Because there are 26 letters (2×13) in the basic Latin alphabet, ROT13 is its own inverse; that is, to undo ROT13, the same algorithm is applied, so the same action can be used for encoding and decoding. The algorithm provides virtually no cryptographic security, and is often cited as a canonical example of weak encryption.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/ROT13)

## XOR
In cryptography, the simple XOR cipher is a type of additive cipher, an encryption algorithm that operates according to the principles:

A ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  0 = A,
A ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  A = 0,
(A ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  B) ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  C = A ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  (B ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  C),
(B ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  A) ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  A = B ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  0 = B,
where ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  denotes the exclusive disjunction (XOR) operation. This operation is sometimes called modulus 2 addition (or subtraction, which is identical). With this logic, a string of text can be encrypted by applying the bitwise XOR operator to every character using a given key. To decrypt the output, merely reapplying the XOR function with the key will remove the cipher.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/XOR_cipher)

[bubble-toptal]: https://www.toptal.com/developers/sorting-algorithms/bubble-sort
[bubble-wiki]: https://en.wikipedia.org/wiki/Bubble_sort
[bubble-image]: https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Bubblesort-edited-color.svg/220px-Bubblesort-edited-color.svg.png "Bubble Sort"

[bucket-wiki]: https://en.wikipedia.org/wiki/Bucket_sort
[bucket-image-1]: https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Bucket_sort_1.svg/311px-Bucket_sort_1.svg.png "Bucket Sort"
[bucket-image-2]: https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Bucket_sort_2.svg/311px-Bucket_sort_2.svg.png "Bucket Sort"

[cocktail-shaker-wiki]: https://en.wikipedia.org/wiki/Cocktail_shaker_sort
[cocktail-shaker-image]: https://upload.wikimedia.org/wikipedia/commons/e/ef/Sorting_shaker_sort_anim.gif "Cocktail Shaker Sort"

[insertion-toptal]: https://www.toptal.com/developers/sorting-algorithms/insertion-sort
[insertion-wiki]: https://en.wikipedia.org/wiki/Insertion_sort
[insertion-image]: https://upload.wikimedia.org/wikipedia/commons/7/7e/Insertionsort-edited.png "Insertion Sort"

[quick-toptal]: https://www.toptal.com/developers/sorting-algorithms/quick-sort
[quick-wiki]: https://en.wikipedia.org/wiki/Quicksort
[quick-image]: https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif "Quick Sort"

[radix-wiki]: https://en.wikipedia.org/wiki/Radix_sort

[merge-toptal]: https://www.toptal.com/developers/sorting-algorithms/merge-sort
[merge-wiki]: https://en.wikipedia.org/wiki/Merge_sort
[merge-image]: https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif "Merge Sort"

[selection-toptal]: https://www.toptal.com/developers/sorting-algorithms/selection-sort
[selection-wiki]: https://en.wikipedia.org/wiki/Selection_sort
[selection-image]: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Selection_sort_animation.gif/250px-Selection_sort_animation.gif "Selection Sort Sort"

[shell-toptal]: https://www.toptal.com/developers/sorting-algorithms/shell-sort
[shell-wiki]: https://en.wikipedia.org/wiki/Shellsort
[shell-image]: https://upload.wikimedia.org/wikipedia/commons/d/d8/Sorting_shellsort_anim.gif "Shell Sort"

[topological-wiki]: https://en.wikipedia.org/wiki/Topological_sorting

[linear-wiki]: https://en.wikipedia.org/wiki/Linear_search
[linear-image]: http://www.tutorialspoint.com/data_structures_algorithms/images/linear_search.gif "Linear Search"

[binary-wiki]: https://en.wikipedia.org/wiki/Binary_search_algorithm
[binary-image]: https://upload.wikimedia.org/wikipedia/commons/f/f7/Binary_search_into_array.png "Binary Search"


[caesar]: https://upload.wikimedia.org/wikipedia/commons/4/4a/Caesar_cipher_left_shift_of_3.svg "Caesar"

[ROT13-image]: https://upload.wikimedia.org/wikipedia/commons/3/33/ROT13_table_with_example.svg "ROT13"

[JumpSearch-image]: https://i1.wp.com/theoryofprogramming.com/wp-content/uploads/2016/11/jump-search-1.jpg "Jump Search"

[QuickSelect-image]: https://upload.wikimedia.org/wikipedia/commons/0/04/Selecting_quickselect_frames.gif "Quick Select"
