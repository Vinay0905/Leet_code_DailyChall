# arr=list(map(int,input().split()))
nums=[2,2,1]
def singleNumber(nums):
    seen=set()
    for i in nums:
        if i in seen:
            seen.remove(i)
        else:
            seen.add(i)
    return seen.pop()

print(singleNumber(nums))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))