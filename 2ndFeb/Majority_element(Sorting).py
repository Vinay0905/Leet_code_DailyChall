nums=[3,2,3]
# Sorting Solution 
def majorityElement(nums):
    nums.sort()
    l=len(nums)
    n=nums[l//2]
    return n
print(majorityElement(nums))