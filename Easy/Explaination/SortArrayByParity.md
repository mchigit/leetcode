## 905. Sort Array By Parity

### Question Description
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

### Examples
```
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

### Solution

**Brute Force:**

Create a new list to hold the result. Loop through original list, if element is odd, then append it to the new list. 
If element is even, prepend it. 

**Optimized:**

Have 2 pointers, start at first element, end at last element. The idea is to increment start pointer to the first odd element,
decrement end pointer to the first even element. Then swap them. All that is left is to find out the condition of the while loop,
which is basically the bounds of array and `start < end`. 

Optimized solution will have `O(n)` at worst case, no additional memory used because swap is in place. 


```python
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) <= 1:
            return A
        
        start, end = 0, len(A) - 1
        while start < end and start < len(A) - 1 and end >= 0:
            # move start pointer to an odd number
            while start < len(A) and A[start] % 2 == 0:
                start += 1

            # move end pointer to an even number
            while end >= 0 and A[end] % 2 != 0:
                end -= 1
            # at this point start should be at odd number, end at even number
            if start < end:
                self.swap(A, start, end)
    
        return A
        
    def swap(self, L: List[int], a: int, b: int):
        temp = L[a];
        L[a] = L[b]
        L[b] = temp
```