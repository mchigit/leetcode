from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        length = len(A)
        evenPointer, oddPointer = 0, 1
        if length <= 1:
            return A

        while oddPointer < length and evenPointer < length:
            while oddPointer < length and A[oddPointer] % 2 == 1:
                oddPointer += 2
            while evenPointer < length and A[evenPointer] % 2 == 0:
                evenPointer += 2

            if oddPointer < length and evenPointer < length:
                self.swap(A, oddPointer, evenPointer)

        return A

    def swap(self, L: List[int], a: int, b: int):
        temp = L[a];
        L[a] = L[b]
        L[b] = temp


if __name__ == '__main__':
    A = [2,3,2,2,5,7,9,8]
    print(Solution().sortArrayByParityII(A));