## 26. Remove Duplicates from Sorted Array

### Question Description
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

### Examples
```
Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
```

### Solution

**Brute Force:**

Create a new list that only stores the unique numbers. But the question prevents us from doing that. 

**Optimized:**

There are several things that we notice from the problem description:

1. The array is sorted, that means if there is a duplicate number, it must be to the right of the current number. So we will always be comparing the elements side by side. 
2. The first element is ALWAYS unique
3. We need to keep track of where to place the unique element. 

Once these 3 points are known, the algorithm is pretty easy to come up with. We have a pointer to keep track of where to place the unique elements, then loop through the entire array, comparing current element with the element after. If `A[i + 1] !== A[i]` then we put `A[i+1]` at index. 
In the end we just return index. 


[Python Code](../Array/RemoveDupFromArray.py)