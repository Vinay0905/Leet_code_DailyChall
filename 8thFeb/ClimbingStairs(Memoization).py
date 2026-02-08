def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(i: int) -> int:
            if i <= 1:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = helper(i - 1) + helper(i - 2)
            return memo[i]
        return helper(n)


# Test cases
test_cases_memo = [2, 3, 4, 5]
print("Memoization Approach Tests:")
for n in test_cases_memo:
    print(f"n={n}: {climbStairs(n)}")