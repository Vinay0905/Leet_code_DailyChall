from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - mid - 1 >= k:
                right = mid - 1
            else:
                left = mid + 1
        return arr[left - 1] + (k - (arr[left - 1] - (left - 1) - 1)) if left > 0 else k
