def climb_stairs_dp(n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]


test_cases_dp = [2, 3, 4, 5]
print("DP Approach Tests:")
for n in test_cases_dp:
    print(f"n={n}: {climb_stairs_dp(n)}")