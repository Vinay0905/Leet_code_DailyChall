nums=[2,2,1]
def singleNumber(nums):
    xor=0
    for i in nums:
        xor^=i
    return xor
print(singleNumber(nums))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))