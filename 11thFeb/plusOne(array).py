from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits
        return [1] + digits


# Example usage:
solution = Solution()       
digits = [1, 2, 3]
result = solution.plusOne(digits)
print(result)  # Output: [1, 2, 4]