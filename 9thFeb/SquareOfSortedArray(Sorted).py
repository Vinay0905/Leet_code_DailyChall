nums_1=[-4,-1,0,3,10]
nums_2= [-7,-3,2,3,11]
def sortedSquares(nums):
    squares = [num * num for num in nums]
    squares.sort()
    return squares


print(sortedSquares(nums_1))
print(sortedSquares(nums_2))

#