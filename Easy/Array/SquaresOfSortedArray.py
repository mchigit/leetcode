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
