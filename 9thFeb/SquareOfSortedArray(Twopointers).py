nums_1=[-4,-1,0,3,10]
nums_2= [-7,-3,2,3,11]
def sortedSquares(nums):
    result = []
    left, right = 0, len(nums) - 1
    while left <= right:
        left_sq = nums[left] * nums[left]
        right_sq = nums[right] * nums[right]
        if left_sq > right_sq:
            result.append(left_sq)
            left += 1
        else:
            result.append(right_sq)
            right -= 1
    return result[::-1]


print(sortedSquares(nums_1))
print(sortedSquares(nums_2))