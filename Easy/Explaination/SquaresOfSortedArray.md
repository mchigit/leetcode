## 977. Squares of a Sorted Array

### Question Description
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

*Note*: 
- 1 <= A.length <= 10000
- -10000 <= A[i] <= 10000
- A is sorted in non-decreasing order.

### Examples
```
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
```

```
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

### Solution

**Brute Force:**

Square each element in the array, the perform sort. `O(n + nlogn)`

**Optimized:**

Notice the pattern: 0 is the mid point of the given array, elements to the left of 0 are all negative and will become positive after squaring them. 
We can have 2 pointers, positive starting at the first positive element, and negative = positive - 1, which is the last negative element in the array.

Looping through the array, compare the squares of elements at both pointers, append the smaller one to a new result array. 
The condition of the loop is basically the array bound. `positive < length and negative >= 0`. After the first while loop ends, check for edge cases by bringing positive pointer
to end of array, and negative pointer to start of the array.

Easy 2-pointer problem, the key is to start in the middle of the array and expand.

- Runtime: `O(n)`
- Memory: `O(n)` because we created a new list


```python
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        length = len(A)
        result = []

        positive = 0
        while positive < length and A[positive] < 0:
            positive += 1

        negative = positive - 1

        while positive < length and negative >= 0:
            positive_square = A[positive] * A[positive]
            negative_square = A[negative] * A[negative]

            if positive_square < negative_square:
                result.append(positive_square)
                positive += 1
            else:
                result.append(negative_square)
                negative -= 1

        while positive < length:
            positive_square = A[positive] * A[positive]
            result.append(positive_square)
            positive += 1

        while negative >= 0:
            negative_square = A[negative] * A[negative]
            result.append(negative_square)
            negative -= 1

        return result
```