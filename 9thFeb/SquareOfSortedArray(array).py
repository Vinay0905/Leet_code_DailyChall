nums_1=[-4,-1,0,3,10]
nums_2= [-7,-3,2,3,11]
def sortedSquares(nums):
    
    return sorted([num * num for num in nums])


print(sortedSquares(nums_1))
print(sortedSquares(nums_2))