import math
def climbStairs(n):
    if n==0 or n==1:
        return 1
    phi=(1+math.sqrt(5))/2
    psi=(1-math.sqrt(5))/2
    return int((phi**(n+1)-psi**(n+1))/math.sqrt(5))


test_cases_math = [2, 3, 4, 5]
print("Math Approach Tests:")
for n in test_cases_math:
    print(f"n={n}: {climbStairs(n)}")