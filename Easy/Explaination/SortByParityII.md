## 905. Sort Array By Parity II

### Question Description
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

### Examples
```
Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
```

### Solution


**Optimized:**

This is another 2 pointers problem, except they both start at the beginning and go to the end.
Realize that we are now trying to swap elements that are out of place with their index, so we can have 2 pointers
indicating elements that are out of place. 

We can do that by having an even pointer and an odd pointer, even starts at 0 and odd starts at 1. Each incrementing by 2 
if they don't find an element that is out of place. So the general algorithm is to have a while loop, move even pointer
to the first odd element on an even index, and move odd pointer to the first even element on an odd index, and swap and loop. 
The condition to end the loop is boundaries. 

Runtime: `O(n)`, actually it's less than that about `O(half n)`


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