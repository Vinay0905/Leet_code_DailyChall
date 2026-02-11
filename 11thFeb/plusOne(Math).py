
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))
        num += 1
        return [int(d) for d in str(num)]


# Example usage:
solution = Solution()       
digits = [1, 2, 3]
result = solution.plusOne(digits)
print(result)