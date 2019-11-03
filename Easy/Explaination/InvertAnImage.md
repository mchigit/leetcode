## Invert an Image

### Question Description
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping `[1, 1, 0]` horizontally results in `[0, 1, 1]`.

To invert an image means that each 0 is replaced by 1, 
and each 1 is replaced by 0. For example, inverting `[0, 1, 1]` results in `[1, 0, 0]`.

*Note*: 
- 1 <= A.length = A[0].length <= 20
- 0 <= A[i][j] <= 1

### Examples
```
Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
```

```
Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
```

### Solution

There is no better way other than looping through each array element in the matrix. There will at least be 2 `for` loops. 
But one way to optimize, is to realize that we don't need to loop through the entire array (Array here means a single array element in the matrix). 

Flipping the image is essentially swapping first and last element, then second and second last element and so on...
Therefore, we only need to loop through half of the array

To optimize, we can combine swapping and inverting in the same operation, which are both constant time. 

There is an edge case: when length of the array is odd, the middle element is not inverted. So we just check specifically for this case

```python
from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            self.swapAndInvert(A[i])
        return A

    def swapAndInvert(self, L: List[int]) -> List[int]:
        endIndex = len(L) // 2
        for i in range(endIndex):
            temp = self.invert(L[i])
            L[i] = self.invert(L[len(L) - i - 1])
            L[len(L) - i - 1] = temp
        if len(L) % 2 == 1:
            # length of the array is odd, invert middle element
            L[len(L) // 2] = self.invert(L[len(L) // 2])
        return L

    def invert(self, num: int) -> int:
        if num == 1:
            return 0
        return 1



if __name__ == '__main__':
    matrix = [[1,1,0],[1,0,1],[0,0,0]]
    print(Solution().flipAndInvertImage(matrix))
```