# Data Structures and Algos

A collection of data structures and algos implemented in Python.


# Sorting algorithms

- Bubble sort
- Selection sort
- Insertion sort
- Merge sort
- Quicksort
- Heapsort
- Counting sort


## Bubble sort

Traverse the array, compare adjacent elements and bubble the highest value to the end of the array. Sorts in place.

- Time: O(n^2)
- Space: O(1)

Use when the array is partially or mostly sorted, this algorithm can be faster than others.


PROs:
- simple implementation
- can quickly sort an array that is mostly sorted

CONs:
- very slow on a typical unsorted array O(n^2)


## Selection sort

Divide the Array into 2 subsets - a sorted and unsorted subset. The algorithm finds the smallest (or largest) element in the unsorted subset and swaps it with the leftmost unsorted element and moving the subset boundary one element to the right.

- Time: O(n^2) average, best and worst
- Space: O(1)

It outperforms Bubble Sort, but is usually worse than Insertion sort. The main advantage of Select Sort is that it does at most `n` swaps (memory write). Insertion sort on the other hand does O(n^2) writes. This can be critical if memory-write operation is significantly more expensive than memory-read ops, such as flash memory.


PROs:
- simple implementation
- faster than bubble sort
- does at most `n` writes which makes it suitable for situation when writing to memory is considered a much more expensive operation than reading

CONs:
- worse than Insertion Sort


## Insertion sort

Insertion sort is a stable, in-place sorting algorithm that builds the final sorted array one item at a time. It is not the very best in terms of performance but more efficient traditionally than most other simple O(n2) algorithms such as selection sort or bubble sort.

- Time: O(n^2), worst: O(n^2) (if the list is reversed), best: O(n)
- Space: O(1) and O(n) in recursive implementation

It is also a well known **online algorithm** since it can sort a list as it receives it. In all other algorithms, we need all elements to be provided to the sorting algorithm before applying it. With insertion sort, we can start we a partial set of elements and sort them. Then insert more elements and sort them. In the real world, data to be sorted is usually not static, rather dynamic. If even one additional element is inserted during the sorting process, other algorithms don't respond easily. But only insertion sort algorithm is not interrupted and can respond well with the additional element

The idea is to divide the array into two subsets - sorted subset and unsorted subsets. For each iteration, insertion sort removes the next element from the unsorted subset, finds the location it belongs within the sorted subset and inserts it there.

PROs:
- **Online alogirthm**, ie can sort a list as it receives the elements. Suitable for applications when the full list is not known in advance or where elements arrive over time.

CONs:
- Still fairly slow O(n^2)


## Merge sort

Merge sort divides a large array into two smaller subarrays and then recursively sorts the subarrays.

- Time:  O(n.log(n)) average, worst O(n^2)
- Space: O(n) for the call stack

External merge sort typically uses a hybrid sort-merge strategy. In the sorting phase, chunks of data small enough to fit in main memory are read, sorted, and written out to a temporary file. In the merge phase, the sorted subfiles are combined into a single larger file.

PROs:
- fast with O(n.log(n))
- works very well as an external sorter when data cannot be fit into memory, ie it is suitable for very large datasets
- stable

CONs:
- generally slower than Quicksort
- not in place, requires additional memory


## Quicksort

Quicksort is an efficient in-place sorting algorithm, which usually performs about two to three times faster than mergesort and heapsort when implemented well. It is a comparison sort, meaning that it can sort items of any type for which a less-than relation is defined. In efficient implementations, it is usually not a stable sort.

Quicksort selects a pivot value and moves smaller values before it and larger values above it.

- Time:  O(n.log(n)) average, worst O(n^2)
- Space: O(n) for the call stack

PROs:
- fastest sorting algorithm O(n.log(n))
- good locality of reference (cache)
- in place

CONs:
- does not guarantee O(n.log(n)), in worst case scenarios it can be O(n^2)
- swaps elements around and can be more expensive than merge sort if the data does not fully fit into memory
- unstable

## Heapsort

PROs:
- although generally slower than quicksort, it guarantees O(n.log(n)) time (with a higher constant factor)

CONs:
- todo

## Counting sort

## Bonus: When to use a Min or Max-Heap:


Use it whenever you need quick access to the largest (or smallest) item, because that item will always be the first element in the array or at the root of the tree.

However, the remainder of the array is kept partially unsorted. Thus, instant access is only possible to the largest (smallest) item. Insertions are fast, so it's a good way to deal with incoming events or data and always have access to the earliest/biggest.

Useful for priority queues, schedulers (where the earliest item is desired), etc...

A heap is a tree where a parent node's value is larger than that of any of its descendant nodes.

If you think of a heap as a binary tree stored in linear order by depth, with the root node first (then the children of that node next, then the children of those nodes next); then the children of a node at index N are at 2N+1 and 2N+2. This property allows quick access-by-index. And since heaps are manipulated by swapping nodes, this allows for in-place sorting.


