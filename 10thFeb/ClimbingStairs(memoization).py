class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i: int) -> int:
            if i <= 1:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = dfs(i - 1) + dfs(i - 2)
            return memo[i]
        return dfs(n)

# Example usage:
solution = Solution()   
n = 5
result = solution.climbStairs(n)
print(f"Number of ways to climb {n} stairs: {result}")  # Output: 8