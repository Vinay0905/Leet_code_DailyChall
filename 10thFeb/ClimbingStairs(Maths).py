class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        prev2, prev = 1, 1
        for _ in range(2, n + 1):
            curr = prev + prev2
            prev2, prev = prev, curr
        return prev


# Example usage:
solution = Solution()
n = 5
result = solution.climbStairs(n)
print(f"Number of ways to climb {n} stairs: {result}")  # Output: 8