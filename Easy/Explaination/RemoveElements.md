## 27. Remove Element

### Question Description
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

### Examples
```
Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
```

### Solution

**Optimized:**

Fairly simple 2 pointers problem. Have 2 pointers, `i` starts at index 0, and `last` starts at `len(nums) - 1`

The idea is to loop through the array, but mainly using the last pointer. 
Check whether the element at first pointer is same as `val`, if it's the same, then swap it with the element at last pointer. Decrement last pointer and repeat. The only time we increment `i` is when `A[i] != val`, this indicates we can move the pointer forward. The while loop will end when first pointer meets second one. 

We then return `last + 1` because when the while loop ends, last will be at the last element of the array that doesn't contain `val`. Need to add 1 because array starts with index of 0. 

[Python Code](../Array/RemoveElements.py)