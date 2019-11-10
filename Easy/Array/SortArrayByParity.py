from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # [2, 4, 2, 5, 1, 2, 4, 5, 1]
        # [2, 4, 2, 4, 1, 2, 5, 5, 1]
        # [2, 4, 2, 4, 2, 1, 5, 1, 1]
        # declare start pointer at first element, end pointer at second element
        # increment start until finding an odd, decrement end until finding an even
        # swap elements
        # Stop when start meets end, or out of bound
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


if __name__ == '__main__':
    arr = [1, 1, 1, 1]

    print(Solution().sortArrayByParity(arr))


